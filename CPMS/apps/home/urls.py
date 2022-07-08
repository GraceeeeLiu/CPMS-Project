# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('toggle/', views.toggle, name='toggle'),
    path('assignmentView/', views.assignmentView, name='assignmentView'),
    path('createReview/<int:pid>/<int:rid>', views.createReview, name='createReview'),
    path('matchAdmin/', views.matchAdmin, name='matchAdmin'),
    path('reviewPaper/', views.reviewPaper, name='reviewPaper'),
    path('reviewForm/<int:pk>', views.reviewForm, name='reviewForm'),
    path('submitForm/<int:pk>', views.submitForm, name='submitForm'),
    path('submitPaper/', views.submitPaper, name='submitPaper'),
    path('newPaper/', views.uploadNewPaper, name='uploadNewPaper'),
    path('', views.defaultHome, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
