#sprc application urls

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game', views.game, name='game'),
    path('maker', views.maker, name='maker')
]