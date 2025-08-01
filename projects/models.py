from django.db import models
from django.contrib.auth.models import User


def generateImagePath(instance, filename):
    return f'image/projects/{instance.user.username}/{filename}'



# Create your models here.
class Project(models.Model):
    class ProjectStatus(models.TextChoices):
        Pending = 'Pending', 'Pending'
        InProgress = 'InProgress', 'InProgress'
        Completed = 'Completed', 'Completed'
        Cancelled = 'Cancelled', 'Cancelled'
        
    class PriorityOptions(models.TextChoices):
        Low = 'Low', 'Low'
        Medium = 'Medium', 'Medium'
        High = 'High', 'High'
        
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    start_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=ProjectStatus.choices, default=ProjectStatus.Pending)
    priority = models.CharField(max_length=10, choices=PriorityOptions.choices, default=PriorityOptions.Medium)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='projects')
    assigned_to = models.ManyToManyField(User,max_length=30, blank=True, null=True, related_name='assigned_projects')
    image = models.ImageField(upload_to=generateImagePath, blank=True, null=True, default='default.png')
    
    def __str__(self):
        return self.title
    
    
    