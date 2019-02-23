#sprc application urls

from django.urls import path
from . import views

urlpatterns = [
    path('', views.brawl, name='brawl'),
]