from django.urls import path

from . import views

urlpatterns = [
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/<slug:slug>/', views.room, name='room'),
]
