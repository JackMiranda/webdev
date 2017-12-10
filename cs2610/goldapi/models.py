# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Converter(models.Model):
    conversion = {
        'stone': 6350.2932, 
        'lbs': 453.59237, 
        't_oz': 31.103477, 
        'ton': 907184.74, 
        'kg': 1000
    }
