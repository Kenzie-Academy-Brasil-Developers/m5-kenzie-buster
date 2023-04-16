from rest_framework import permissions
from users.models import User

class EmployeePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS or request.user.is_authenticated and request.user.is_superuser
        )
        
class OrdersPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True
        
class UserOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: User):
        return obj.owner == request.user
    
class IsAdmOrUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        if request.user.is_authenticated and request.user.id == int(view.kwargs["user_id"]):
            return True