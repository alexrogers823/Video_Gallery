from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('edit/', views.edit_video, name='edit')
]
