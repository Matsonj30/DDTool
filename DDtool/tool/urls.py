from django.urls import path
from . import views



urlpatterns = [
    path('/<str:ticker>', views.getInfo, name='infoPage'),
    path('', views.home, name='home-page'),



]