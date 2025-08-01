from rest_framework import routers
from .viewsets import ProjectViewSet

app_name = 'projects'
routers = routers.DefaultRouter()
routers.register('project',ProjectViewSet)
