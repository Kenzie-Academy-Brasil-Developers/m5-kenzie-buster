from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Movie


class IsMovieOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, movie: Movie) -> bool:
        return movie.user == request.user


class IsSuperOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_employee
        )