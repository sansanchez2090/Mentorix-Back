from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from gestor import views

router = routers.DefaultRouter()
router.register(r'skills', views.SkillViewSet, 'skills')
router.register(r'users', views.UserViewSet, 'users')
router.register(r'areas', views.AreaViewSet, 'areas')
router.register(r'projects', views.ProjectViewSet, 'projects')  
router.register(r'project_members', views.ProjectMembersViewSet, 'project_members')
router.register(r'issues', views.IssuesViewSet, 'issues')
router.register(r'tasks', views.TaskViewSet, 'tasks')

# Router anidado para Members bajo Project
projects_router = nested_routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'members', views.ProjectMembersViewSet, basename='project-members')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(projects_router.urls)),
    path('Docs', include_docs_urls(title='Mentorix API Documentation')),
]