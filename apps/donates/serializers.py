from rest_framework import serializers

from apps.donates.models import Donates


class DonatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donates
        fields = "__all__"


class DonatesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donates
        exclude = ['created_at', 'updated_at']
