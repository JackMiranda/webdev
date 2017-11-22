from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^aboot$', views.aboot, name='aboot'),
    url(r'^tech$', views.tech, name='tech'),
    url(r'^archive$', views.archive, name='archive'),
    url(r'^(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<blog_id>[0-9]+)/comment/$', views.comment, name='comment'),
]