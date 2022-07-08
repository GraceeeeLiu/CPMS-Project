# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q


from .models import Paper, Review, Reviewer, Defaults
from .forms import PaperUpdateForm, ReviewUpdateForm, ToggleForm
from .filters import PaperFilter, ReviewFilter, ReviewerFilter


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


## Utilities
class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


## for Authors - Papers

class PaperList(LoginRequiredMixin, FilteredListView):
    model = Paper
    template_name = 'home/submitPaper.html'
    context_object_name = 'paper'

    def get_queryset(self):
        if self.request.user.usercat.usertype == "Author":
            qs = Paper.objects.filter(AuthorID=self.request.user.usercat.author).order_by('Title')
            filterset_class = PaperFilter(self.request.GET, queryset=qs)
            return filterset_class
        elif self.request.user.usercat.usertype == "Admin":
            qs = Paper.objects.all().order_by('Title')
            filterset_class = PaperFilter(self.request.GET, queryset=qs)
            return filterset_class
        else:
            qs = Jobs.objects.none()
            filterset_class = PaperFilter(self.request.GET, queryset=qs)
            return filterset_class

@login_required(login_url="/login/")
def submitPaper(request):
    if request.user.usercat.usertype == "Author":
        paper_list = Paper.objects.filter(AuthorID=request.user.usercat.author).order_by('Title')
        totalCount = paper_list.count()
        filter = PaperFilter(request.GET, queryset=paper_list)
        reviewCount = Review.objects.filter(PaperID__in=paper_list, Complete=True).count()
        if not reviewCount:
            reviewCount = 0
    else:
        paper_list = Paper.objects.none()
        filter = PaperFilter(request.GET, queryset=paper_list)
        reviewCount = 0
        totalCount = 0
    paginator = Paginator(filter.qs, 15)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'title': 'Paper Submissions',
        'header': 'Papers',
        'filter': filter,
        'page_obj': page_obj,
        'count': totalCount,
        'reviewCount': reviewCount,
    }
    return render(request, 'home/submitPaper.html', context)


@login_required(login_url="/login/")
def submitForm(request, pk):
    paper = Paper.objects.get(pk=pk)
    instance = get_object_or_404(Paper, PaperID=pk)
    pform = PaperUpdateForm(request.POST or None, request.FILES or None, instance=instance)
    if request.method == 'POST':
        if pform.is_valid():
            pform.save()
            messages.success(request, f'Paper successfully submitted.')
            return redirect('submitPaper')
        else:
            pform = PaperUpdateForm(instance=instance)

    context = {
        'paper': paper,
        'pform': pform
    }
    return render(request, 'home/submitForm.html', context)

@login_required(login_url="/login/")
def uploadNewPaper(request):
    checkDefault = Defaults.objects.get(pk=1)
    print(checkDefault.EnableReviewers)
    if checkDefault.EnableAuthors:
        paper = Paper.objects.create(AuthorID=request.user.usercat.author)
        paper.save()
        lastPK = paper.pk
        return redirect('submitForm', pk=lastPK)
    else:
        messages.warning(request, f'Admin has disabled Paper submission!')
        return redirect('submitPaper')

###################################
## for Reviewers - Papers - Reviews

class ReviewList(LoginRequiredMixin, FilteredListView):
    model = Review
    template_name = 'home/reviewPaper.html'
    context_object_name = 'review'

    def get_queryset(self):
        if self.request.user.usercat.usertype == "Reviewer":
            qs = Review.objects.filter(ReviewerID=self.request.user.usercat.reviewer)
            filterset_class = ReviewFilter(self.request.GET, queryset=qs)
            return filterset_class
        else:
            qs = Review.objects.none()
            filterset_class = ReviewFilter(self.request.GET, queryset=qs)
            return filterset_class


@login_required(login_url="/login/")
def reviewPaper(request):
    if request.user.usercat.usertype == "Reviewer":
        review_list = Review.objects.filter(ReviewerID=request.user.usercat.reviewer)
        totalCount = review_list.count()
        filter = ReviewFilter(request.GET, queryset=review_list)
        reviewCount = Review.objects.filter(ReviewID__in=review_list, Complete=False).count()
        if not reviewCount:
            reviewCount = 0
    else:
        review_list = Review.objects.none()
        filter = ReviewFilter(request.GET, queryset=review_list)
        reviewCount = 0
        totalCount = 0

    paginator = Paginator(filter.qs, 15)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'title': 'Review Submissions',
        'header': 'Reviews',
        'filter': filter,
        'page_obj': page_obj,
        'count': totalCount,
        'reviewCount': reviewCount,
    }
    return render(request, 'home/reviewPaper.html', context)


def downloadFile(request, path):
    response = HttpResponse(content_type='text')
    response['Content-Disposition'] = "attachment; filename='paper.txt'"
    response['X-Sendfile'] = smart_str(os.path.join(settings.MEDIA_ROOT, path))
    return response



@login_required(login_url="/login/")
def reviewForm(request, pk):
    checkDefault = Defaults.objects.get(pk=1)
    if checkDefault.EnableReviewers:
        review = Review.objects.get(pk=pk)
        instance = get_object_or_404(Review, ReviewID=pk)
        rform = ReviewUpdateForm(request.POST or None, instance=instance)
        if request.method == 'POST':
            if rform.is_valid():
                rform.save()
                messages.success(request, f'Review successfully submitted.')
                return redirect('reviewPaper')
            else:
                rform = ReviewUpdateForm(instance=instance)

        context = {
            'review': review,
            'rform': rform
        }
        return render(request, 'home/reviewForm.html', context)
    else:
        messages.warning(request, f'Admin has disabled access to review papers!')
        return redirect('reviewPaper')
## for Admin Management - Paper, Reviews, Authors, Reviewers


# def matchAdmin(request):
#     paper = Paper.objects.all()
#
#     context = {
#         'test': 'test',
#         'paper': paper,
#     }
#
#     return render(request, 'home/matchAdmin.html', context)
@login_required(login_url="/login/")
def matchAdmin(request):
    if request.user.usercat.usertype == "Admin":
        # paper = Paper.objects.get(pk=pk)
        # instance = get_object_or_404(Paper, PaperID=pk)
        if request.method == "POST":
            paperID = request.POST.get('paperID')
            reviewerID = request.POST.get('reviewerID')

            if paperID or reviewerID:
                if Paper.objects.filter(PaperID=paperID).exists():
                    pInstance = get_object_or_404(Paper, PaperID=paperID)
                else:
                    pInstance = None
                    messages.warning(request, f'The PaperID input does not EXIST!')
                    return redirect('matchAdmin')

                if Reviewer.objects.filter(ReviewerID=reviewerID).exists():
                    rInstance = get_object_or_404(Reviewer, ReviewerID=reviewerID)
                else:
                    rInstance = None
                    messages.warning(request, f'The ReviewerID input does not EXIST!')
                    return redirect('matchAdmin')

                if pInstance and rInstance:
                    reviewOBJ = Review.objects.create(PaperID=pInstance, ReviewerID=rInstance)
                    reviewOBJ.save()

                    countPaper = Review.objects.filter(PaperID=paperID).count()
                    if countPaper > 3:
                        lastPK = reviewOBJ.pk
                        Review.objects.filter(ReviewID=lastPK).delete()
                        messages.warning(request, f'Assignment Fail: Each paper can only be assigned at Maximum: 3 Reviewers!')
                        return redirect('matchAdmin')
                    else:
                        messages.success(request, f'Assignment Successfully Submitted!.')
                        return redirect('matchAdmin')

                else:
                    messages.warning(request, f'Assignment Failed, please check your assignment input values!')
                    return redirect('matchAdmin')
            else:
                messages.info(request, f'No input values were passed to the Assignment Form...')
                redirect('matchAdmin')
            # check if any is empty. if empty. print error message
            # if not empty create object for review

        reviewer = Reviewer.objects.all()
        papers = Paper.objects.all()
        if request.user.usercat.usertype == "Admin":
            paper_list = Paper.objects.all().order_by('Title')
            totalCount = paper_list.count()
            filter = PaperFilter(request.GET, queryset=paper_list)
            reviewCount = Review.objects.filter(PaperID__in=paper_list, Complete=True).count()
            if not reviewCount:
                reviewCount = 0

            reviewer_list = Reviewer.objects.all()
            filter1 = ReviewerFilter(request.GET, queryset=reviewer_list)

        else:
            paper_list = Paper.objects.none()
            filter = PaperFilter(request.GET, queryset=paper_list)
            reviewCount = 0
            totalCount = 0

            reviewer_list = Reviewer.objects.none()
            filter1 = ReviewerFilter(request.GET, queryset=reviewer_list)

        paginator = Paginator(filter.qs, 10)
        page = request.GET.get('page')


        ## for Paper Table
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        paginator1 = Paginator(filter1.qs, 10)
        page1 = request.GET.get('page1')

        ## for Reviewers Table
        try:
            page_obj1 = paginator1.page(page1)
        except PageNotAnInteger:
            page_obj1 = paginator1.page(1)
        except EmptyPage:
            page_obj1 = paginator1.page(paginator1.num_pages)


        context = {
            'title': 'Admin Papers',
            'header': 'Papers',
            'filter': filter,
            'filter1': filter1,
            'page_obj': page_obj,
            'page_obj1': page_obj1,
            'reviewer': reviewer,
            'papers': papers,
            'count': totalCount,
            'reviewCount': reviewCount,
        }
        return render(request, 'home/matchAdmin.html', context)
    elif request.user.usercat.usertype == "Author":
        return redirect("submitPaper")
    elif request.user.usercat.usertype == "Reviewer":
        return redirect("reviewPaper")

#gracedanielcpms
@login_required(login_url="/login/")
def createReview(request, pid, rid):
    review = Review.objects.create(PaperID=pid, ReviewerID=rid)
    review.save()
    #lastPK = review.pkcr

    return redirect('matchAdmin')

@login_required(login_url="/login/")
def assignmentView(request):
    #assignedReviews = Review.objects.all()

    if request.user.usercat.usertype == "Admin":
        assignedReviews = Review.objects.all()
        filter = ReviewFilter(request.GET, queryset=assignedReviews)

        #####countings
        # total papers submitted
        allPapers =  Paper.objects.all()
        totalPaper = allPapers.count()
        # assigned
        totalCount = assignedReviews.count()
        # reviewed
        reviewed = Review.objects.filter(ReviewID__in=assignedReviews, Complete=True).count()
        # unreviewed
        unreviewed = Review.objects.filter(ReviewID__in=assignedReviews, Complete=False).count()
        # unassigned
        unassigned = Review.objects.filter(~Q(PaperID__in=allPapers)).distinct().count()
        # unassigned = totalPaper-unassigned

        # use this to get the number of papers unassigned
        # reviewCount = Review.objects.filter(ReviewID__in=assignedReviews, Complete=False).count()
        # if not reviewCount:
        #     reviewCount = 0
    else:
        assignedReviews = Review.objects.none()
        filter = ReviewFilter(request.GET, queryset=review_list)
        reviewCount = 0
        totalCount = 0
        reviewed = 0
        unreviewed = 0
        totalPaper = 0
        unassigned = 0
    paginator = Paginator(filter.qs, 20)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'title': 'Assigned Papers',
        'header': 'Reviews',
        'filter': filter,
        'page_obj': page_obj,
        'count': totalCount,
        'reviewed': reviewed,
        'unreviewed': unreviewed,
        'totalPaper': totalPaper,
        'unassigned': unassigned,
        # 'reviewCount': reviewCount,
    }
    return render(request, 'home/assignmentView.html', context)

@login_required(login_url="/login/")
def defaultHome(request):
    if request.user.usercat.usertype == "Admin":
        return redirect('assignmentView')
    elif request.user.usercat.usertype == "Reviewer":
        return redirect('reviewPaper')
    elif request.user.usercat.usertype == "Author":
        return redirect('submitPaper')


def toggle(request):
    default = Defaults.objects.get(pk=1)

    instance = get_object_or_404(Defaults, pk=1)
    rform = ToggleForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if rform.is_valid():
            rform.save()
            messages.success(request, f'Toggle Submitted!')
            return redirect('toggle')
        else:
            rform = ToggleForm(instance=instance)

    context = {
        'default': default,
        'rform': rform
    }
    return render(request, 'home/toggle.html', context)

