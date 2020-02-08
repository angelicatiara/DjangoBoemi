
from django.urls import path
from HelloDjangoApp import views

urlpatterns = [
    path('', views.HelloDjangoApp, name='HelloDjangoApp'),
    ]