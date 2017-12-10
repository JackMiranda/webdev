# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.forms import ModelForm, Textarea

import datetime

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=50)
    content = models.TextField(max_length = 2000)
    posted_date = models.DateTimeField('date posted')
    def __str__(self):
        return self.content
    def was_published_recently(self):
        return self.posted_date >= timezone.now() - datetime.timedelta(days = 1)

class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commenter_nickname = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField(max_length=1000)
    posted_date = models.DateTimeField('date commented')
    def __str__(self):
        return self.content
        


# Create your models here.