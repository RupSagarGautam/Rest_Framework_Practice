from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    class RoleOptions(models.TextChoices):
        Employer = 'Employer', 'Employer'
        Worker = 'Worker', 'Worker'
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=RoleOptions.choices, default=RoleOptions.Worker)
    address = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
