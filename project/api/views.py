from rest_framework import generics
from .serializers import ProjectUserSerializer, ProjectModelSerializer
from project.models import ProjectModel, ProjectUsers


class ProjectCreateAPIView(generics.CreateAPIView):
    serializer_class = ProjectModelSerializer
    queryset = ProjectModel.objects.all()

    def perform_create(self, serializer):
        project_owner = self.request.user.ProjectUser
        serializer.save(project_owner=project_owner)


class ProjectListAPIView(generics.ListAPIView):
    serializer_class = ProjectModelSerializer
    queryset = ProjectModel.objects.all()


class ProjectUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProjectModelSerializer
    queryset = ProjectModel.objects.all()
    lookup_field = 'slug'


class ProjectDeleteAPIView(generics.DestroyAPIView):
    permission_classes = []
    serializer_class = ProjectModelSerializer
    queryset = ProjectModel.objects.all()
    lookup_field = 'slug'
