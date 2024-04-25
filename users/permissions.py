from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User

class IsUserOwnerAuthenticated (permissions.BasePermission):
  def has_object_permission(self, request: Request, view: View, obj):
    if  request.user.is_superuser:
        return True
    
    return obj.id == request.user.id

  