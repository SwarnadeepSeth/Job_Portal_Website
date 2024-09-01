# teachers/forms.py
from django import forms
from .models import TeacherProfile

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = [
            'first_name',
            'last_name',
            'affiliation',
            'qualifications',
            'about',
            'hourly_rate',
            'picture',
            'website',
            'phone_number',
            'email',
            'country',
            'area',
            'availability',
        ]
