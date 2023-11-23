from rest_framework.generics import UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from apps.heroes.models import Heroes, UserHeroes
from apps.heroes.serializers import HeroesSerializer, HeroesCreateSerializer, UserHeroesSerializer, \
    UserHeroesCreateSerializer


class HeroesListViewSet(ListAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializer


class HeroesCreateViewSet(CreateAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesCreateSerializer
    permission_classes = [AllowAny]


class HeroesDeleteViewSet(DestroyAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializer
    permission_classes = [AllowAny]


class HeroesUpdateViewSet(UpdateAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesCreateSerializer
    permission_classes = [AllowAny]


class HeroesDetailViewSet(RetrieveAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializer
    permission_classes = [AllowAny]


class UserHeroesCreateViewSet(CreateAPIView):
    queryset = UserHeroes.objects.all()
    serializer_class = UserHeroesCreateSerializer
    permission_classes = [AllowAny]


class UserHeroesDeleteViewSet(DestroyAPIView):
    queryset = UserHeroes.objects.all()
    serializer_class = UserHeroesSerializer
    permission_classes = [AllowAny]


class UserHeroesUpdateViewSet(UpdateAPIView):
    queryset = UserHeroes.objects.all()
    serializer_class = UserHeroesCreateSerializer
    permission_classes = [AllowAny]


class UserHeroesDetailViewSet(RetrieveAPIView):
    queryset = UserHeroes.objects.all()
    serializer_class = UserHeroesSerializer
    permission_classes = [AllowAny]
