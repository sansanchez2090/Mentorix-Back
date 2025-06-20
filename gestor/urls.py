from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from gestor import views

router = routers.DefaultRouter()
router.register(r'skills', views.SkillViewSet, 'skills')
router.register(r'users', views.UserViewSet, 'users')
router.register(r'areas', views.AreaViewSet, 'areas')
router.register(r'projects', views.ProjectViewSet, 'projects')  
router.register(r'project_members', views.ProjectMembersViewSet, 'project_members')
router.register(r'issues', views.IssuesViewSet, 'issues')
router.register(r'tasks', views.TaskViewSet, 'tasks')

urlpatterns = [
    path('api/', include(router.urls)),
    path('Docs', include_docs_urls(title='Mentorix API Documentation')),
]