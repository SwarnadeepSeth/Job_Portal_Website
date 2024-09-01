from django.db import models
from django.contrib.auth.models import User

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=100, default='Unknown')  # Provide a default value
    qualifications = models.CharField(max_length=100)
    about = models.TextField(default='No information provided')  # Provide a default value
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    picture = models.ImageField(upload_to='teacher_pictures/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    availability = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
