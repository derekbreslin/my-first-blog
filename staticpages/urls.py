from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('calendar/', views.calendar, name='calendar'),
    path('testtournament/', views.testtournament, name='testtournament'),
]

