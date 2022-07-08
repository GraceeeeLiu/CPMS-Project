# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Paper, Review, Defaults

from decimal import Decimal

class PaperUpdateForm(forms.ModelForm):
    PaperID = forms.IntegerField(disabled=True, widget=forms.HiddenInput())

    FilenameOriginal = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)

    Filename = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)
    Title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)
    Certification = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)
    NotesToReviewers = forms.CharField(
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
    fileLOC = forms.FileField(required=False)
    class Meta:
        model = Paper
        fields = ['PaperID', 'FilenameOriginal', 'Filename', 'Title', 'Certification', 'NotesToReviewers',
                  'AnalysisOfAlgorithms',
                  'Applications', 'Architecture', 'ArtificialIntelligence', 'ComputerEngineering', 'Curriculum',
                  'DataStructures', 'Databases',
                  'DistanceLearning', 'DistributedSystems', 'EthicalSocietalIssues', 'FirstYearComputing',
                  'GenderIssues', 'GrantWriting',
                  'GraphicsImageProcessing', 'HumanComputerInteraction', 'LaboratoryEnvironments', 'Literacy',
                  'MathematicsInComputing',
                  'Multimedia', 'NetworkingDataCommunications', 'NonMajorCourses', 'ObjectOrientedIssues',
                  'OperatingSystems', 'ParallelProcessing',
                  'Pedagogy', 'ProgrammingLanguages', 'Research', 'Security', 'SoftwareEngineering',
                  'SystemsAnalysisAndDesign', 'UsingTechnologyInTheClassroom',
                  'WebAndInternetProgramming', 'Other', 'OtherDescription', 'fileLOC']


class ReviewUpdateForm(forms.ModelForm):
    ReviewID = forms.IntegerField(disabled=True, widget=forms.HiddenInput())

    AppropriatenessOfTopic = forms.DecimalField(required=False, decimal_places=2, max_digits=3)
    TimelinessOfTopic = forms.DecimalField(required=False, decimal_places=2, max_digits=3)
    SupportiveEvidence = forms.DecimalField(required=False, decimal_places=2, max_digits=3)
    TechnicalQuality = forms.DecimalField(required=False, decimal_places=2, max_digits=3)
    ScopeOfCoverage = forms.DecimalField(required=False, decimal_places=2, max_digits=3)
    CitationOfPreviousWork = forms.DecimalField(required=False, decimal_places=2, max_digits=3)
    Originality = forms.DecimalField(required=False, decimal_places=2, max_digits=3)
    ContentComments = forms.DecimalField(required=False, decimal_places=2, max_digits=3)
    OrganizationOfPapers = forms.DecimalField(required=False, decimal_places=2, max_digits=3)
    ClarityOfMainMessage = forms.DecimalField(required=False, decimal_places=2, max_digits=3)
    Mechanics = forms.DecimalField(required=False, decimal_places=2, max_digits=3)

    WrittenDocumentComments = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)

    SuitabilityForPresentation = forms.DecimalField(required=False, decimal_places=2, max_digits=3)
    PotentialInterestInTopic = forms.DecimalField(required=False, decimal_places=2, max_digits=3)

    PotentialForOralPresentationComments = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)


    OverallRating = forms.DecimalField(required=False, decimal_places=2, max_digits=3)

    OverallRatingComments = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ), required=False)

    ComfortLevelTopic = forms.DecimalField(required=False, decimal_places=2, max_digits=3)
    ComfortLevelAcceptability = forms.DecimalField(required=False, decimal_places=2, max_digits=3)
    Complete = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = Review
        fields = ['ReviewID', 'AppropriatenessOfTopic', 'TimelinessOfTopic','SupportiveEvidence','TechnicalQuality','ScopeOfCoverage','CitationOfPreviousWork',
                  'Originality','ContentComments','OrganizationOfPapers','ClarityOfMainMessage','Mechanics','WrittenDocumentComments','SuitabilityForPresentation',
                  'PotentialInterestInTopic','PotentialForOralPresentationComments','OverallRating','OverallRatingComments','ComfortLevelTopic','ComfortLevelAcceptability','Complete']




class MatchUpdateForm(forms.ModelForm):
    PaperID = forms.IntegerField(required=False)
    ReviewerID = forms.IntegerField(required=False)

    class Meta:
        model = Review
        fields = ['PaperID', 'ReviewerID']



class ToggleForm(forms.ModelForm):
    EnableReviewers = forms.ChoiceField(required=False, choices=Defaults.rchoices)
    EnableAuthors = forms.ChoiceField(required=False, choices=Defaults.achoices)
    class Meta:
        model = Defaults
        fields = ['EnableReviewers', 'EnableAuthors']













