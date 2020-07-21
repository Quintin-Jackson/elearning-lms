from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('jan_mohr/', views.jan_mohr, name='jan_mohr'),
    path('error/', views.error, name='error'),
]
