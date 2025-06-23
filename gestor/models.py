from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=200)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skill = models.CharField(max_length=200, default="")
    skills = models.ManyToManyField('Skill', related_name='users')

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    area_members = models.ManyToManyField(User, related_name='areas')

    def __str__(self):
        return self.name 

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    client = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    team_members = models.PositiveSmallIntegerField(default=0)
    members = models.ManyToManyField(User, related_name='projects', through='ProjectMembers')
    project_type = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProjectMembers(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    role = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["project", "user"], name="unique_project_user"
            )
        ] 
    
    def __str__(self):
        return f"{self.user.name} - {self.project.name} ({self.role})"

class Issues(models.Model):
    ISSUE_STATUS_CHOICES = {
        'P': 'Pendiente',
        'C': 'Completado',
        'E': 'En progreso',
    }
    name = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  
    status = models.CharField(max_length=1, choices=ISSUE_STATUS_CHOICES, default='P')

    def __str__(self):
        return f"{self.name} - {self.project.name} ({self.get_status_display()})"

class Task(models.Model):
    TASK_STATUS_CHOICES = {
        'P': 'Pendiente',
        'C': 'Completado',
        'E': 'En progreso',
    }
    name = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    deadline = models.DateField()  
    status = models.CharField(max_length=1, choices=TASK_STATUS_CHOICES, default='P')

    def __str__(self):
        return f"{self.name} - {self.project.name} ({self.get_status_display()})"   

class Skill(models.Model):
    description = models.TextField(default="")
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name