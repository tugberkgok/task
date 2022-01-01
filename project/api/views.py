from rest_framework import generics
from .serializers import ProjectUserSerializer, ProjectModelSerializer
from project.models import ProjectModel, ProjectUsers
from rest_framework.filters import SearchFilter
from .paginations import SmallPagination
from .permissions import IsOwnerOrIsAdminOrReadOnly, IsIsAdminOrReadOnly
from rest_framework.permissions import IsAdminUser


class ProjectCreateAPIView(generics.CreateAPIView):
    serializer_class = ProjectModelSerializer
    queryset = ProjectModel.objects.all()

    def perform_create(self, serializer):
        project_owner = self.request.user.ProjectUser
        serializer.save(project_owner=project_owner)


class ProjectListAPIView(generics.ListAPIView):
    serializer_class = ProjectModelSerializer
    pagination_class = (SmallPagination)

    def get_queryset(self):
        print(self.request.user.is_active)
        if self.request.user.is_active == True:
            if self.request.user.ProjectUser.admin is True:
                queryset = ProjectModel.objects.all()
                return queryset
            elif self.request.user.ProjectUser.admin is False:
                queryset = ProjectModel.objects.filter(project_owner=self.request.user.ProjectUser)
                return queryset
        else:
            queryset = []
            return queryset


class ProjectUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProjectModelSerializer
    permission_classes = [IsOwnerOrIsAdminOrReadOnly]
    queryset = ProjectModel.objects.all()
    lookup_field = 'slug'


class ProjectDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsIsAdminOrReadOnly]
    serializer_class = ProjectModelSerializer
    queryset = ProjectModel.objects.all()
    lookup_field = 'slug'


class ProjectUserUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProjectUserSerializer
    permission_classes = [IsAdminUser]
    queryset = ProjectUsers.objects.all()



