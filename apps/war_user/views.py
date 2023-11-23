from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from apps.war_user.models import WarUser
from apps.war_user.serializers import WarUserSerializer, WarUserCreateSerializer


class WarUserCreateViewSet(CreateAPIView):
    queryset = WarUser.objects.all()
    serializer_class = WarUserCreateSerializer
    permission_classes = [AllowAny]


class WarUserDeleteViewSet(DestroyAPIView):
    queryset = WarUser.objects.all()
    serializer_class = WarUserSerializer
    permission_classes = [AllowAny]


class WarUserUpdateViewSet(UpdateAPIView):
    queryset = WarUser.objects.all()
    serializer_class = WarUserCreateSerializer
    permission_classes = [AllowAny]


class WarUserDetailViewSet(RetrieveAPIView):
    queryset = WarUser.objects.all()
    serializer_class = WarUserSerializer
    permission_classes = [AllowAny]
