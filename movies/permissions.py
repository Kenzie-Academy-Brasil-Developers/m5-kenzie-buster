from rest_framework import permissions
from rest_framework.views import Request, View


class IsEmployeeOrReadOnly(permissions.BasePermission):
    def has_permisssion(self, request: Request, view: View):
        import ipdb

        ipdb.set_trace()
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_employee
