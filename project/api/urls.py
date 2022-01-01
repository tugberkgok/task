from django.urls import path, include
from .views import ProjectCreateAPIView, ProjectListAPIView, ProjectUpdateAPIView, ProjectDeleteAPIView

urlpatterns = [
    path('create', ProjectCreateAPIView.as_view(), name='create'),
    path('list', ProjectListAPIView.as_view(), name='list'),
    path('update/<slug>', ProjectUpdateAPIView.as_view(), name='update'),
    path('delete/<slug>', ProjectDeleteAPIView.as_view(), name='delete'),
    path('api-auth/', include('rest_framework.urls')),
]
