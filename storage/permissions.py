from rest_framework.permissions import BasePermission


class IsManager(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.filter(name="managers").first())
