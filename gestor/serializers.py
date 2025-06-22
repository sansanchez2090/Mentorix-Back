from rest_framework import serializers
from .models import *

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(many=True, read_only=True,slug_field='name')

    class Meta:
        model = User
        fields = ['name', 'description','skills', 'resume']
        extra_kwargs =  {'ID': {'write_only': True},
                         'password': {'write_only': True},
                         'resume': {'read_only': True}
                        }

class AreaSerializer(serializers.ModelSerializer):
    area_members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Area
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        exclude = ['members']

class ProjectMembersSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(source='project', read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    user = UserSerializer(read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = ProjectMembers
        fields = ['project_id','user_id','user_name','user','role']

class IssuesSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(source='project', read_only=True)
    assigned_to = serializers.SlugRelatedField(read_only=True, slug_field='name')
    status = serializers.ChoiceField(choices=Issues.ISSUE_STATUS_CHOICES)

    class Meta:
        model = Issues
        fields = ['project_id', 'name', 'assigned_to','status']

class TaskSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(source='project', read_only=True)
    assigned_to = serializers.SlugRelatedField(read_only=True, slug_field='name')
    status = serializers.ChoiceField(choices=Task.TASK_STATUS_CHOICES)

    class Meta:
        model = Task
        fields = ['project_id','name','assigned_to','deadline','status']