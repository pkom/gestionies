# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import Course

# Register your models here.
# pre django 1.7
#admin.site.register(Course)

# django 1.7+
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
