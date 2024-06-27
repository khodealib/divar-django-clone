from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from accounts.serializers import UserRegistarionSerializer


class UserRegisterView(generics.CreateAPIView):
    """Register a new user

    Args:
    UserRegisterView (generics.CreateAPIView): Register a new user.
    """

    serializer_class = UserRegistarionSerializer
    queryset = User.objects.all()


class UserChangePasswordView(generics.UpdateAPIView):
    """Update user password

    Args:
    UserChangePasswordView (generics.UpdateAPIView): Update user password.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = UserRegistarionSerializer
    queryset = User.objects.all()
