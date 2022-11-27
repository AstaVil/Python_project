from django.urls import path
from . import views


urlpatterns = [
    path('taskposts/', views.taskpost_list, name='taskpost_list'),
    path('taskpost/upload', views.upload_taskpost, name='upload_taskpost'),
    path('taskpost/<int:id>/', views.delete_taskpost, name='delete_taskpost'),
    ]
