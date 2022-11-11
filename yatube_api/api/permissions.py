from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    message = 'Только автор может менять контент'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
