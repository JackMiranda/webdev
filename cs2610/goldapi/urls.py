from django.conf.urls import url
from . import views

app_name = "goldapi"
urlpatterns = [
        url(r'^$',views.convertAPI, name='convertAPI'),
]
