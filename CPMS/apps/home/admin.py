# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Paper, Review, Defaults
# Register your models here.


class PaperAdminModel(admin.ModelAdmin):
    search_fields = ('FilenameOriginal', )

class ReviewAdminModel(admin.ModelAdmin):
    search_fields = ('FilenameOriginal', )


class DefaultAdminModel(admin.ModelAdmin):
    search_fields = ('EnableAuthors', )

admin.site.register(Paper, PaperAdminModel)
admin.site.register(Review, ReviewAdminModel)
admin.site.register(Defaults, DefaultAdminModel)