# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Converter
import json

# Create your views here.

def convert(value, ufrom, uto):
    value = Converter.conversion[ufrom] * value
    value = value / Converter.conversion[uto]
    return value
        
def convertAPI(request):
    
    resp = {}
    
    if not request.GET.has_key('from') or not request.GET.has_key('to') or not request.GET.has_key('value'):
        resp['error'] = "Usage: to=[unit] from=[unit] value=[floating point number]"
    else:
        mto = request.GET['to']
        mfrom = request.GET['from']
        mvalue = float(request.GET['value'])
        result = convert(uto=mto,ufrom=mfrom,value=mvalue)
        resp = { "units":mto, "value":result }
        
    return HttpResponse(json.dumps(resp))
                