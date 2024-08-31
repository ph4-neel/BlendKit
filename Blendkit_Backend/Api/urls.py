from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('college/',College.as_view()),
    path('department/',Department.as_view()),
    path('Student/',Student.as_view()),
]