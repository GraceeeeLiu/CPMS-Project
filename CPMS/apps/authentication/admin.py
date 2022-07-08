# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Author, Reviewer, UserCAT

# Register your models here.
class TypeAdminModel(admin.ModelAdmin):
    search_fields = ('user',)

class AuthorAdminModel(admin.ModelAdmin):
    search_fields = ('user',)

class ReviewerAdminModel(admin.ModelAdmin):
    search_fields = ('user',)

admin.site.register(UserCAT, TypeAdminModel)
admin.site.register(Author, AuthorAdminModel)
admin.site.register(Reviewer, ReviewerAdminModel)

