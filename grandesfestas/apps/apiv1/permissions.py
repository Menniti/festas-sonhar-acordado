# -*- coding: utf-8 -*-
from rest_framework import permissions


class AuthOrWriteOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        if request.method in ('PUT', 'POST', 'PATCH',):
            return True

        # Instance must have an attribute named `owner`.
        return request.user and request.user.is_authenticated()
