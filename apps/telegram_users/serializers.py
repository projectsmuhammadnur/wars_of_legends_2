from rest_framework import serializers

from apps.telegram_users.models import TelegramUsers, UserToUsers


class TelegramUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUsers
        fields = "__all__"


class TelegramUsersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUsers
        exclude = ['created_at', 'updated_at']


class UserToUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToUsers
        fields = "__all__"


class UserToUsersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToUsers
        exclude = ['created_at', 'updated_at']
