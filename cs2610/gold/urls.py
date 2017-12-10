from django.conf.urls import url
from . import views

app_name = "gold"
urlpatterns = [
        url(r'^$',views.goldWeight, name='gold'),
]
