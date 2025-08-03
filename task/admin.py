from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'priority', 'created_at', 'updated_at')
    search_fields = ('title', 'user__username')
    list_filter = ('status', 'priority', 'created_at')


admin.site.register(Task, TaskAdmin)
    