from rest_framework import serializers

from accounts.models import User


class UserRegistarionSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False, max_length=255)
    last_name = serializers.CharField(required=False, max_length=255)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = User(**validated_data)
        password = validated_data.get("password")
        user.set_password(password)
        user.save()
        return user
