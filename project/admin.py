from django.contrib import admin
from .models import ProjectModel, ProjectUsers

# Register your models here.

admin.site.register(ProjectModel)
admin.site.register(ProjectUsers)

