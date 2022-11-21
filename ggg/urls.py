from django.urls import path

from . import views


urlpatterns = [
    path('gggtournament/', views.gggtournament, name='gggtournament'),

    path('testtournament/', views.testtournament, name='testtournament'),

    path('gggtournament/new/', views.new_entry, name='new_entry'),
]