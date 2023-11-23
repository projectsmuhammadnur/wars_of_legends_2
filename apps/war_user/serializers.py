from rest_framework import serializers

from apps.war_user.models import WarUser


class WarUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarUser
        fields = "__all__"


class WarUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarUser
        exclude = ['created_at', 'updated_at']