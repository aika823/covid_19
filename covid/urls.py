from django.urls import path
from . import views

app_name = 'covid'

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('effect/', views.effect, name='effect'),
    path('survey/', views.survey, name='survey'),
    path('vaccination/', views.vaccination, name='vaccination'),
    path('create/', views.create, name='create'),
]