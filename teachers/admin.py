from django.contrib import admin
from .models import TeacherProfile

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'qualifications', 'hourly_rate', 'email', 'phone_number', 'country', 'area', 'availability')
    search_fields = ('user__username', 'email', 'country', 'area')
 
