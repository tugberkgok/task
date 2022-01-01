from rest_framework import serializers
from project.models import ProjectModel, ProjectUsers


class ProjectModelSerializer(serializers.ModelSerializer):
    project_owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProjectModel
        fields = '__all__'


class ProjectUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUsers
        fields = '__all__'

