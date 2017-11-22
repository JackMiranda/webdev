# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Blog, Comments
from django.template import loader
from django.urls import reverse

import time
from django.utils import timezone


def tech(request):
    curTime = time.strftime("%c")
    template = loader.get_template('blog/tech.html')
    context = {
        'curTime': curTime,
    }
    return HttpResponse(template.render(context,request))

def aboot(request):
    curTime = time.strftime("%c")
    template = loader.get_template('blog/aboot.html')
    context = {
        'curTime': curTime,
    }
    return HttpResponse(template.render(context,request))

def archive(request):
    curTime = time.strftime("%c")
    blog_list = Blog.objects.order_by('-posted_date') 
    template = loader.get_template('blog/archive.html')
    context = {
        'blog_list': blog_list,
        'curTime': curTime,
    }
    return HttpResponse(template.render(context,request))

def index(request):
    curTime = time.strftime("%c")
    latest_blog_list = Blog.objects.order_by('-posted_date')[:3] 
    template = loader.get_template('blog/index.html')
    context = {
        'latest_blog_list': latest_blog_list,
        'curTime': curTime,
    }
    return HttpResponse(template.render(context,request))

def detail(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog post does not exist")
    return render(request, 'blog/detail.html', {'blog': blog})

def comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    try:
        blog.comments_set.create(content=request.POST.get('commentbody', None),
                                 commenter_nickname=request.POST.get('nickname',None),
                                 email=request.POST.get('email',None),
                                 posted_date=timezone.now())
    except (KeyError, Comments.DoesNotExist):
        return render(request, 'blog/detail.html', {
            'blog': blog,
            'error_message': "You, uh, failed to comment",
        })
    else:
        blog.save()
    return HttpResponseRedirect(reverse('blog:detail',args=(blog.id,)))

# Create your views here.
