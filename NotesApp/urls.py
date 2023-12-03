from django.urls import path

from NotesApp import views

app_name = "NotesApp"

urlpatterns = [
    path('', views.Create)
