from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListServicioTipo.as_view()),
    path('detail/<pk>/', views.DetailServicioTIpo.as_view()),
    path('add/', views.CreateServicioTipo.as_view()),
    path('update/<pk>/', views.UpdateServicioTipo.as_view()),
    path('delete/<pk>/', views.DeleteServicioTipo.as_view()),
]
