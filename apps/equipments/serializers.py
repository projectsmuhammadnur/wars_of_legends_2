from rest_framework import serializers

from apps.equipments.models import Equipments, UserEquipments


class EquipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipments
        fields = "__all__"


class EquipmentsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipments
        exclude = ['created_at', 'updated_at']


class UserEquipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEquipments
        fields = "__all__"


class UserEquipmentsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEquipments
        exclude = ['created_at', 'updated_at']
