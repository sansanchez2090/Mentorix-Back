from rest_framework import viewsets
from gestor import serializers
from gestor import models

# Create your views here.
class SkillViewSet(viewsets.ModelViewSet):
    queryset = models.Skill.objects.all()
    serializer_class = serializers.SkillSerializer 

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return models.User.objects.all().prefetch_related('skills', 'projects')

class AreaViewSet(viewsets.ModelViewSet):
    queryset = models.Area.objects.all()
    serializer_class = serializers.AreaSerializer   

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer

class ProjectMembersViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectMembers.objects.all()
    serializer_class = serializers.ProjectMembersSerializer 

    def get_queryset(self):
        project_pk = self.kwargs.get('project_pk') # Usamos get() para evitar KeyError si no está presente

        # Si project_pk está presente, filtramos los miembros por ese proyecto
        if project_pk:
            return models.ProjectMembers.objects.filter(project=project_pk)
        # Si no hay project_pk en la URL, devolvemos todos los miembros (o puedes lanzar un error)
        else:
            return models.ProjectMembers.objects.all() # O podrías lanzar una excepción: raise ValueError("Project ID is required.")


class IssuesViewSet(viewsets.ModelViewSet):
    queryset = models.Issues.objects.all()
    serializer_class = serializers.IssuesSerializer

    def get_queryset(self):
        return models.Issues.objects.filter(assigned_to=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        return models.Task.objects.filter(assigned_to=self.request.user)