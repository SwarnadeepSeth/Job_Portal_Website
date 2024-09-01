# teachers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),  # List of teachers
    path('create/', views.create_teacher_profile, name='teacher_profile_create'),  # Create teacher profile
]
