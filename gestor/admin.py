from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Area)
admin.site.register(Project)
admin.site.register(ProjectMembers)
admin.site.register(Issues)
admin.site.register(Task)
admin.site.register(Skill)
