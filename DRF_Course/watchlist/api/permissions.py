from rest_framework import permissions

class AdminOrReadonly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        adminpermission= bool(request.user and request.user.is_staff)

        return request.method == "GET" or adminpermission

class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user
