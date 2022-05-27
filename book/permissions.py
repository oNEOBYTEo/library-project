from rest_framework import permissions


class IsLibrarian(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        is_staff = request.user.is_staff == True
        return is_staff