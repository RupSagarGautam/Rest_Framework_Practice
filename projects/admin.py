from django.contrib import admin

# Register your models here.
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'user')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')
    
admin.site.register(Project, ProjectAdmin)