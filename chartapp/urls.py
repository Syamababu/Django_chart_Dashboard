from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pie/', views.index2, name='Pie'),
    path('line/', views.index3, name='Line'),
    path('nav/', views.index4, name='Nav'),




]