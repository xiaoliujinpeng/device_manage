from rest_framework.permissions import BasePermission


class ApprovePermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method == 'GET' and view.action in ["retrieve", "list"]:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.username == request.user.username
