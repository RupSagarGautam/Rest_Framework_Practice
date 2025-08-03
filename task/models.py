from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.

def generateAttachmentPath(instance, filename):
    return f'attachments/tasks/{instance.user.username}/{filename}'


class Task(models.Model):
    class statusOptions(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        INPPROGRESS = 'InProgress', 'InProgress'
        COMPLETED = 'Completed', 'Completed'
        CANCELLED = 'Cancelled', 'Cancelled'
        
    class priorityOptions(models.TextChoices):
        LOW = 'Low', 'Low'
        MEDIUM = 'Medium', 'Medium'
        HIGH = 'High', 'High'
        
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ManyToManyField(User, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', blank=True, null=True) 
    status = models.CharField(max_length=15, choices=statusOptions.choices, default=statusOptions.PENDING)
    priority = models.CharField(max_length=10, choices=priorityOptions.choices, default=priorityOptions.MEDIUM)
    attachment = models.FileField(upload_to=generateAttachmentPath, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return self.title