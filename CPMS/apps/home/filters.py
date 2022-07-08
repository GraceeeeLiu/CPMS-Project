import django_filters
from django_filters import CharFilter, ChoiceFilter , DateFromToRangeFilter, DateFilter, RangeFilter, BooleanFilter
from django.forms.widgets import TextInput, DateInput, Select
from django_filters.widgets import RangeWidget
from django.db import models
from .models import Paper, Review, Reviewer


class PaperFilter(django_filters.FilterSet):

    activeFilter = ChoiceFilter(field_name='Active', choices=Paper.choices)
    filenameSearch = CharFilter(field_name='Filename', lookup_expr='icontains', label='Filename', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'File Name', 'size': 20, }))
    TitleSearch = CharFilter(field_name='Title', lookup_expr='icontains', label='Title',  widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'size': 20, }))
    certificationSearch = CharFilter(field_name='Certification', lookup_expr='icontains', label='Certification',  widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Certification', 'size': 20, }))
    affiliationSearch = CharFilter(field_name='AuthorID__Affiliation', lookup_expr='icontains', label='Affiliation', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Affiliation', 'size': 20, }))
    departmentSearch = CharFilter(field_name='AuthorID__Department', lookup_expr='icontains', label='Affiliation', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Department', 'size': 20, }))



class ReviewFilter(django_filters.FilterSet):

    #completeFilter = BooleanFilter(choices=Review.choices, field_name='Complete')
    completeFilter = ChoiceFilter(field_name='Complete', choices=Review.choices)
    ReviewSearch = CharFilter(field_name='ReviewID', lookup_expr='icontains', label='ReviewID', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'ReviewID', 'size': 20, }))
    filenameSearch = CharFilter(field_name='PaperID__Filename', lookup_expr='icontains', label='Filename', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'File Name', 'size': 20, }))
    TitleSearch = CharFilter(field_name='PaperID__Title', lookup_expr='icontains', label='Title',widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'size': 20, }))
    certificationSearch = CharFilter(field_name='PaperID__Certification', lookup_expr='icontains', label='Certification',widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Certification', 'size': 20, }))
    departmentSearch =  CharFilter(field_name='PaperID__AuthorID__Department', lookup_expr='icontains', label='Department',widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Department', 'size': 20, }))
    affiliationSearch =  CharFilter(field_name='PaperID__AuthorID__Affiliation', lookup_expr='icontains', label='Affiliation',widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Affiliation', 'size': 20, }))
    ## made for the admin usage - change the loop in reviewPaper.html
    firstSearch = CharFilter(field_name='PaperID__AuthorID__AuthorID__userID__first_name', lookup_expr='icontains', label='First Name',widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'size': 20, }))
    lastSearch = CharFilter(field_name='PaperID__AuthorID__AuthorID__userID__last_name', lookup_expr='icontains',label='Last Name', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'size': 20, }))

    # TitleSearch = CharFilter(field_name='Title', lookup_expr='icontains', label='Title',  widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'size': 20, }))
    # certificationSearch = CharFilter(field_name='Certification', lookup_expr='icontains', label='Certification',  widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Certification', 'size': 20, }))


class ReviewerFilter(django_filters.FilterSet):
    activeFilter = ChoiceFilter(field_name='Active', choices=Reviewer.choices)
    acknowledgedFilter = ChoiceFilter(field_name='ReviewsAcknowledged', choices=Reviewer.ack)
    reviewerSearch = CharFilter(field_name='ReviewerID', lookup_expr='exact', label='ReviewerID', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'ReviewerID', 'size': 20, }))
    reviewerName = CharFilter(field_name='ReviewerID__userID__first_name', lookup_expr='icontains', label='First Name', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'size': 20, }))
    reviewerLast = CharFilter(field_name='ReviewerID__userID__last_name', lookup_expr='icontains', label='Last Name', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'size': 20, }))
    reviewerAffiliation = CharFilter(field_name='ReviewerID__Affiliation', lookup_expr='icontains', label='Affiliation', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Affiliation', 'size': 20, }))
    reviewerDepartment = CharFilter(field_name='ReviewerID__Department', lookup_expr='icontains', label='Department', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Department', 'size': 20, }))

