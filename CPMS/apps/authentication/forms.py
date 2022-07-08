# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Author, Reviewer, USERTYPE


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    firstname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))

    lastname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ))

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email']


# class AuthorUpdateForm(forms.ModelForm):
#
#     class Meta:
#         model = Author
#         fields = ['MiddleInitial']



#, 'Type', 'MiddleInitial', 'Affiliation', 'Department', 'Address', 'City', 'State', 'ZipCode', 'PhoneNumber'


class AuthorUpdateForm(forms.ModelForm):
    MiddleInitial = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)

    Affiliation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)

    Department = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)
    Address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)
    City = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)
    State = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)
    ZipCode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)
    PhoneNumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)

    class Meta:
        model = Author
        fields = ['MiddleInitial', 'Affiliation', 'Department', 'Address', 'City', 'State', 'ZipCode', 'PhoneNumber']



class ReviewerUpdateForm(forms.ModelForm):
    MiddleInitial = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)

    Affiliation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)

    Department = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)
    Address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)
    City = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)
    State = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)
    ZipCode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)
    PhoneNumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)

    AnalysisOfAlgorithms = forms.BooleanField(required=False, initial=False)
    Applications = forms.BooleanField(required=False, initial=False)
    Architecture = forms.BooleanField(required=False, initial=False)
    ArtificialIntelligence = forms.BooleanField(required=False, initial=False)
    ComputerEngineering = forms.BooleanField(required=False, initial=False)
    Curriculum = forms.BooleanField(required=False, initial=False)
    DataStructures = forms.BooleanField(required=False, initial=False)
    Databases = forms.BooleanField(required=False, initial=False)
    DistanceLearning = forms.BooleanField(required=False, initial=False)
    DistributedSystems = forms.BooleanField(required=False, initial=False)
    EthicalSocietalIssues = forms.BooleanField(required=False, initial=False)
    FirstYearComputing = forms.BooleanField(required=False, initial=False)
    GenderIssues = forms.BooleanField(required=False, initial=False)
    GrantWriting = forms.BooleanField(required=False, initial=False)
    GraphicsImageProcessing = forms.BooleanField(required=False, initial=False)
    HumanComputerInteraction = forms.BooleanField(required=False, initial=False)
    LaboratoryEnvironments = forms.BooleanField(required=False, initial=False)
    Literacy = forms.BooleanField(required=False, initial=False)
    MathematicsInComputing = forms.BooleanField(required=False, initial=False)
    Multimedia = forms.BooleanField(required=False, initial=False)
    NetworkingDataCommunications = forms.BooleanField(required=False, initial=False)
    NonMajorCourses = forms.BooleanField(required=False, initial=False)
    ObjectOrientedIssues = forms.BooleanField(required=False, initial=False)
    OperatingSystems = forms.BooleanField(required=False, initial=False)
    ParallelProcessing = forms.BooleanField(required=False, initial=False)
    Pedagogy = forms.BooleanField(required=False, initial=False)
    ProgrammingLanguages = forms.BooleanField(required=False, initial=False)
    Research = forms.BooleanField(required=False, initial=False)
    Security = forms.BooleanField(required=False, initial=False)
    SoftwareEngineering = forms.BooleanField(required=False, initial=False)
    SystemsAnalysisAndDesign = forms.BooleanField(required=False, initial=False)
    UsingTechnologyInTheClassroom = forms.BooleanField(required=False, initial=False)
    WebAndInternetProgramming = forms.BooleanField(required=False, initial=False)
    Other = forms.BooleanField(required=False, initial=False)
    OtherDescription = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ), required=False)
    ReviewsAcknowledged = forms.BooleanField(required=False, initial=False)






    class Meta:
        model = Reviewer
        fields = ['MiddleInitial', 'Affiliation', 'Department', 'Address', 'City', 'State', 'ZipCode', 'PhoneNumber', 'AnalysisOfAlgorithms',
                  'Applications','Architecture','ArtificialIntelligence','ComputerEngineering','Curriculum','DataStructures','Databases',
                  'DistanceLearning','DistributedSystems','EthicalSocietalIssues','FirstYearComputing','GenderIssues','GrantWriting',
                  'GraphicsImageProcessing','HumanComputerInteraction','LaboratoryEnvironments','Literacy','MathematicsInComputing',
                  'Multimedia','NetworkingDataCommunications','NonMajorCourses','ObjectOrientedIssues','OperatingSystems','ParallelProcessing',
                  'Pedagogy','ProgrammingLanguages','Research','Security','SoftwareEngineering','SystemsAnalysisAndDesign','UsingTechnologyInTheClassroom',
                  'WebAndInternetProgramming','Other','OtherDescription','ReviewsAcknowledged']


