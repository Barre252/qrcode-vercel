from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# User Model 'Extended'
class CustomUser(AbstractUser):
    tell = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
         return self.username
    
class VisitorRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    person_to_visit = models.CharField(max_length=30)
    visit_reason = models.TextField()
    hours_to_stay = models.IntegerField(null=True, help_text="Enter the number of hours you plan to stay")
    visit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name