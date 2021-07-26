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


class DevicePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method == 'GET' and view.action in ["retrieve", "list"]:
            return True
        elif request.method == 'POST' and view.action in ['get_all']:
            return True
        elif request.method == 'PUT' and view.action in ['update']:
            return True
        elif view.action in ['apply_borrow', 'apply_return']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return True


class LocationPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif view.action in ['retrieve', 'list']:
            return True
        else:
            return False
    def has_object_permission(self, request, view, obj):
        return True
