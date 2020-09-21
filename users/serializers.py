from rest_framework import serializers
from users.models import CustomUser
from django.utils import timezone

class UsersSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=254)
    class_teacher = serializers.CharField(max_length=1)
    is_superuser = serializers.BooleanField(default=False)
    is_staff = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=True)
    date_joined = serializers.DateTimeField(default=timezone.now)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)
