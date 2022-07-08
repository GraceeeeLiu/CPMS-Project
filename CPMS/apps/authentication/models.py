# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

USERTYPE = (
    ('Author','Author'),
    ('Reviewer','Reviewer'),
    ('Admin','Admin'),
)


class UserCAT(models.Model):
    userID = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField(blank=True, null=True, choices=USERTYPE, max_length=20)
    def __str__(self):
        return str(self.userID.username)

# Create your models here.
class Reviewer(models.Model):
    choices = ((True, 'Active'), (False, 'Inactive'), (None, 'Undetermined'))
    ack = ((True, 'Yes'), (False, 'No'), (None, 'Undetermined'))
    ReviewerID = models.OneToOneField(UserCAT, on_delete=models.CASCADE)
    Active = models.BooleanField(choices=choices, null=True, default=True)

    MiddleInitial = models.CharField(blank=True, null=True, max_length=1)

    Affiliation = models.CharField(blank=True, null=True, max_length=50)
    Department = models.CharField(blank=True, null=True, max_length=50)
    Address = models.CharField(blank=True, null=True, max_length=50)
    City = models.CharField(blank=True, null=True, max_length=50)
    State = models.CharField(blank=True, null=True, max_length=2)
    ZipCode = models.CharField(blank=True, null=True, max_length=10)
    PhoneNumber = models.CharField(blank=True, null=True, max_length=50)

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
    ReviewsAcknowledged = models.BooleanField(choices=ack, null=True, default=None)

    def __str__(self):
        return str(self.ReviewerID.userID.username)


class Author(models.Model):
    AuthorID = models.OneToOneField(UserCAT, on_delete=models.CASCADE)
    MiddleInitial = models.CharField(blank=True, null=True, max_length=1)
    Affiliation = models.CharField(blank=True, null=True, max_length=50)
    Department = models.CharField(blank=True, null=True, max_length=50)
    Address = models.CharField(blank=True, null=True, max_length=50)
    City = models.CharField(blank=True, null=True, max_length=50)
    State = models.CharField(blank=True, null=True, max_length=2)
    ZipCode = models.CharField(blank=True, null=True, max_length=10)
    PhoneNumber = models.CharField(blank=True, null=True, max_length=50)


    def __str__(self):
        return str(self.AuthorID.userID.username)
