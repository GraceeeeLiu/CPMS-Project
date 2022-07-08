# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from apps.authentication.models import Author, Reviewer
from django.urls import reverse

# Create your models here.
class Paper(models.Model):
    choices = ((True, 'Active'), (False, 'Inactive'), (None, 'Undetermined'))

    PaperID = models.AutoField(primary_key=True)
    AuthorID = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    Active = models.BooleanField(choices=choices, null=True, default=True)

    FilenameOriginal = models.CharField(blank=True, null=True, max_length=100)
    Filename =  models.CharField(blank=True, null=True, max_length=100)
    Title = models.CharField(blank=True, null=True, max_length=200)
    Certification = models.CharField(blank=True, null=True, max_length=3)
    NotesToReviewers = models.CharField(blank=True, null=True, max_length=255)

    AnalysisOfAlgorithms = models.BooleanField(null=True, default=None)
    Applications = models.BooleanField(null=True, default=None)
    Architecture = models.BooleanField(null=True, default=None)
    ArtificialIntelligence = models.BooleanField(null=True, default=None)
    ComputerEngineering = models.BooleanField(null=True, default=None)
    Curriculum = models.BooleanField(null=True, default=None)
    DataStructures = models.BooleanField(null=True, default=None)
    Databases = models.BooleanField(null=True, default=None)
    DistanceLearning = models.BooleanField(null=True, default=None)
    DistributedSystems = models.BooleanField(null=True, default=None)
    EthicalSocietalIssues = models.BooleanField(null=True, default=None)
    FirstYearComputing = models.BooleanField(null=True, default=None)
    GenderIssues = models.BooleanField(null=True, default=None)
    GrantWriting = models.BooleanField(null=True, default=None)
    GraphicsImageProcessing = models.BooleanField(null=True, default=None)
    HumanComputerInteraction = models.BooleanField(null=True, default=None)
    LaboratoryEnvironments = models.BooleanField(null=True, default=None)
    Literacy = models.BooleanField(null=True, default=None)
    MathematicsInComputing = models.BooleanField(null=True, default=None)
    Multimedia = models.BooleanField(null=True, default=None)
    NetworkingDataCommunications = models.BooleanField(null=True, default=None)
    NonMajorCourses = models.BooleanField(null=True, default=None)
    ObjectOrientedIssues = models.BooleanField(null=True, default=None)
    OperatingSystems = models.BooleanField(null=True, default=None)
    ParallelProcessing = models.BooleanField(null=True, default=None)
    Pedagogy = models.BooleanField(null=True, default=None)
    ProgrammingLanguages = models.BooleanField(null=True, default=None)
    Research = models.BooleanField(null=True, default=None)
    Security = models.BooleanField(null=True, default=None)
    SoftwareEngineering = models.BooleanField(null=True, default=None)
    SystemsAnalysisAndDesign = models.BooleanField(null=True, default=None)
    UsingTechnologyInTheClassroom = models.BooleanField(null=True, default=None)
    WebAndInternetProgramming = models.BooleanField(null=True, default=None)
    Other = models.BooleanField(null=True, default=None)
    OtherDescription = models.CharField(blank=True, null=True, max_length=50)
    fileLOC = models.FileField(blank=True, null=True, upload_to='documents/')
    def __str__(self):
        return str(self.FilenameOriginal)

    def get_absolute_url(self):
        return reverse('submitForm', kwargs={'pk': self.PaperID})

class Review(models.Model):
    choices = ((True, 'Complete'), (False, 'Incomplete'), (None, 'Undetermined'))

    ReviewID = models.AutoField(primary_key=True)
    PaperID = models.ForeignKey(Paper, on_delete=models.CASCADE)
    ReviewerID = models.ForeignKey(Reviewer, on_delete=models.CASCADE)

    AppropriatenessOfTopic = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    TimelinessOfTopic = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    SupportiveEvidence = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    TechnicalQuality = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    ScopeOfCoverage = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    CitationOfPreviousWork = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    Originality = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    ContentComments = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    OrganizationOfPapers = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    ClarityOfMainMessage = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    Mechanics = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    WrittenDocumentComments = models.CharField(blank=True, null=True, max_length=255)
    SuitabilityForPresentation = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    PotentialInterestInTopic = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    PotentialForOralPresentationComments = models.CharField(blank=True, null=True, max_length=255)
    OverallRating = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    OverallRatingComments = models.CharField(blank=True, null=True, max_length=255)
    ComfortLevelTopic = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    ComfortLevelAcceptability = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)
    Complete = models.BooleanField(choices=choices, blank=True, null=True, default=False)

    def __str__(self):
        return str(self.PaperID.FilenameOriginal)

    def get_absolute_url(self):
        return reverse('reviewForm', kwargs={'pk': self.ReviewID})


class Defaults(models.Model):
    rchoices = ((True, 'Enable'), (False, 'Disable'), (None, 'Unset'))
    achoices = ((True, 'Enable'), (False, 'Disable'), (None, 'Unset'))
    EnableReviewers = models.BooleanField(null=False, default=True, choices=rchoices)
    EnableAuthors = models.BooleanField(null=False, default=True, choices=achoices)

    def __str__(self):
        return "Authors: " + str(self.EnableAuthors) + "    Reviewers: "+str(self.EnableReviewers)