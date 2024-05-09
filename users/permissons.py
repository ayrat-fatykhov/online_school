from rest_framework import permissions


class IsModer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists()


class IsCreator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
