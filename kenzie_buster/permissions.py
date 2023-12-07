from rest_framework import permissions
from users.models import User
from rest_framework.views import Request, View


class MyCustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
                request.user.is_authenticated
                and request.user.is_superuser
        )


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return obj == request.user or request.user.is_employee
