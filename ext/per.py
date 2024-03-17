from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class MyPermission1(BasePermission):
    message = {'status': False, 'error': 'NoMyPermission1'}

    def has_permission(self, request, view):
        return True


class MyPermission2(BasePermission):
    message = {'status': False, 'error': 'NoMyPermission2'}

    def has_permission(self, request, view):
        return True