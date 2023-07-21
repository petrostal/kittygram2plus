# cats/permissions.py

from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        # вместо доп класса ReadOnly можно здесь добавит проверку
        # на self.action - если 'retrieve', то вернуть True
        # иначе проверить авторство
        # или так:
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # return obj.author == request.user
        return obj.owner == request.user


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
