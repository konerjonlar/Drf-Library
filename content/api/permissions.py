from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin


class IsBookOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ("update", "delete"):
            return request.user == obj.owner
        return True


class IsCommenterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ("update", "delete"):
            return request.user == obj.from_user
        return True
