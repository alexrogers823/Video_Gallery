from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, 'home'),
    path('/edit', views.edit_video, 'edit')
]
