# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm, AuthorUpdateForm, ReviewerUpdateForm,UserUpdateForm
from .models import Author, Reviewer, UserCAT


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


# def register_user(request):
#     msg = None
#     success = False
#
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=raw_password)
#
#             msg = 'User created - please <a href="/login">login</a>.'
#             success = True
#
#             # return redirect("/login/")
#
#         else:
#             msg = 'Form is not valid'
#     else:
#         form = SignUpForm()
#
#     return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def register_author(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")
            new_type = UserCAT.objects.create(userID=user, usertype="Author")
            new_user = Author.objects.create(AuthorID=new_type)
            new_type.save()
            new_user.save()
        else:
            msg = 'Form is not valid'

    else:
        form = SignUpForm()

    return render(request, "accounts/registerAuthor.html", {"form": form, "msg": msg, "success": success})

def register_reviewer(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")
            new_type = UserCAT.objects.create(userID=user, usertype="Reviewer")
            new_user = Reviewer.objects.create(ReviewerID=new_type, Active=True)
            new_type.save()
            new_user.save()
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/registerReviewer.html", {"form": form, "msg": msg, "success": success})


def profile(request):
    uform = UserUpdateForm(request.POST, instance=request.user)
    usertype = request.user.usercat.usertype
    if usertype == 'Author':
        form1 = AuthorUpdateForm(request.POST, instance=request.user.usercat.author)
        if request.method == 'POST':
            if uform.is_valid() and form1.is_valid():
                uform.save()
                form1.save()
                messages.success(request, f'Account successfully updated.')
                return redirect('profile')
        else:
            uform = UserUpdateForm(instance=request.user)
            form1 = AuthorUpdateForm(instance=request.user.usercat.author)

            # form1 = AuthorUpdateForm(instance=request.user.author)
        context = {
            'uform': uform,
            'form1': form1,
            'usertype': usertype
        }
        return render(request, "home/profile.html", context)

    elif usertype == 'Reviewer':
        form1 = ReviewerUpdateForm(request.POST, instance=request.user.usercat.reviewer)
        if request.method == 'POST':
            if uform.is_valid() and form1.is_valid():
                uform.save()
                form1.save()
                messages.success(request, f'Account successfully updated.')
                return redirect('profile')
        else:
            uform = UserUpdateForm(instance=request.user)
            form1 = ReviewerUpdateForm(instance=request.user.usercat.reviewer)
            # form1 = AuthorUpdateForm(instance=request.user.author)
        context = {
            'uform': uform,
            'form1': form1,
            'usertype': usertype
        }
        return render(request, "home/profile.html", context)

