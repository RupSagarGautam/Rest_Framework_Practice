from rest_framework import serializers
from .models import Project



class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField( read_only=True, many=False, view_name='user-detail')
    assigned_to = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='user-detail')
    
    class Meta:
        model = Project
        fields = [ 'id','user', 'title', 'description', 'image', 'status', 'created_at', 'updated_at',  'priority', 'user', 'assigned_to', 'start_date', 'due_date']