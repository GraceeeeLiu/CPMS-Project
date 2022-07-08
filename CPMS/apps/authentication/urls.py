# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_reviewer, register_author, profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('registerAuthor/', register_author, name="registerAuthor"),
    path('registerReviewer/', register_reviewer, name="registerReviewer"),
    path('profile/', profile, name="profile"),
    path("logout/", LogoutView.as_view(), name="logout")
]
