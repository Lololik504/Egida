from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Permissions


class IsSchoolProfile(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.permission <= Permissions.school.value:
            return True
        else:
            return False


class IsDistrictProfile(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.permission <= Permissions.district.value:
            return True
        else:
            return False
