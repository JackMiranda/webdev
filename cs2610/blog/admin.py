# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Blog, Comments

admin.site.register(Blog)
admin.site.register(Comments)

# Register your models here.
