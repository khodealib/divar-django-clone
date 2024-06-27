from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import UserChangePasswordSerializer, UserRegistarionSerializer


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
    serializer_class = UserChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance, serializer.validated_data)
        return Response(status=status.HTTP_200_OK)
        
