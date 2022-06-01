from django.shortcuts import get_object_or_404
from rest_framework.permissions import SAFE_METHODS, BasePermission


class ItemPermission(BasePermission):
    def has_permission(self, request, view):
        self.message = 'Method "{}" not allowed.'.format(request.method)

        return request.user.is_authenticated and request.auth is not None

    def has_object_permission(self, request, view, item):
        print(view.action)
        if not request.user.is_authenticated:
            return False
        if request.user == item.user:
            return True
        return False