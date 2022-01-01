from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsOwnerOrIsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_active == True:
            if request.method in SAFE_METHODS:
                return True
            elif request.user.ProjectUser.admin is True:
                return True
            return request.user == obj.project_owner
        return False


class IsIsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_active == True:
            if request.method in SAFE_METHODS:
                return True
            elif request.user.ProjectUser.admin is True:
                return True
        return False
