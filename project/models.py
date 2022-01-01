from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# Create your models here.


class ProjectUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ProjectUser')
    admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "User"

    def __str__(self):
        return str(self.username)


class ProjectModel(models.Model):

    project_name = models.CharField(max_length=150)
    project_description = models.TextField()
    starting_date = models.DateTimeField()
    deadline_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='project_name', unique=True)
    project_owner = models.ForeignKey(ProjectUsers, on_delete=models.CASCADE, related_name='projects')

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        db_table = "Project"

    def __str__(self):
        return str(self.project_name)
