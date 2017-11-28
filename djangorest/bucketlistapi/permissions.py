# from rest_framework.permissions import BasePermission
# from .models import Bucket, Bucketlist
#
# class IsOwner(BasePermission):
#     """Custom permission class to allow only bucketlist owners to edit them."""
#
#     def has_object_permission(self, request, view, obj):
#         """Return True if permission is granted to the bucketlist owner."""
#         if isinstance(obj, Bucket):
#             return obj.owner == request.user
#         return obj.owner == request.user

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.created_by == request.user