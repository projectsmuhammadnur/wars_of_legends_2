from rest_framework import serializers

from apps.heroes.models import Heroes, UserHeroes


class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroes
        fields = "__all__"


class HeroesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroes
        exclude = ['created_at', 'updated_at']


class UserHeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHeroes
        fields = "__all__"


class UserHeroesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHeroes
        exclude = ['created_at', 'updated_at']
