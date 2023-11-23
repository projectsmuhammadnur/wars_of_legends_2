from rest_framework import serializers

from apps.wars.models import Wars, WarUsers


class WarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wars
        fields = "__all__"


class WarsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wars
        exclude = ['created_at', 'updated_at']


class WarUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarUsers
        fields = "__all__"


class WarUsersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarUsers
        exclude = ['created_at', 'updated_at']
