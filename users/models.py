from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def generateImagePath(instance, filename):
    return f'profile_images/{instance.user.username}/{filename}'

class Profile(models.Model):
    class RoleOptions(models.TextChoices):
        Employer = 'Employer', 'Employer'
        Worker = 'Worker', 'Worker'
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=RoleOptions.choices, default=RoleOptions.Worker)
    address = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to=generateImagePath, blank=True, null=True, default='default.png')
    
    def __str__(self):
        return f"{self.user.username}'s profile" 