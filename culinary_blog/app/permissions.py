from rest_framework import permissions

class IsChefOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj.chef)
        print(request.user)
        if obj.chef == request.user:
            return True