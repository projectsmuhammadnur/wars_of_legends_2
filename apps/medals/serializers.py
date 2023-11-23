from rest_framework import serializers

from apps.medals.models import Medals, UserMedals


class MedalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medals
        fields = "__all__"


class MedalsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medals
        exclude = ['created_at', 'updated_at']


class UserMedalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMedals
        fields = "__all__"


class UserMedalsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMedals
        exclude = ['created_at', 'updated_at']
