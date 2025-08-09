from rest_framework.permissions import BasePermission
from .models import Advertisement

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.creator == request.user

class IsNotDraftForOthers(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.status != Advertisement.DRAFT:
            return True
        return obj.creator == request.user

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_staff