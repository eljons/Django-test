from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='photos_home'),
]
