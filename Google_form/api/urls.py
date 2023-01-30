from django.contrib import admin
from django.urls import path,include
from index.views import FormAPI

urlpatterns = [
    path('form/',FormAPI.as_view()),
]