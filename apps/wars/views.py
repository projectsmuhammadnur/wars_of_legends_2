from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from apps.wars.models import WarUsers, Wars
from apps.wars.serializers import WarUsersSerializer, WarUsersCreateSerializer, WarsCreateSerializer, WarsSerializer


class WarsCreateViewSet(CreateAPIView):
    queryset = Wars.objects.all()
    serializer_class = WarsCreateSerializer
    permission_classes = [AllowAny]


class WarsDeleteViewSet(DestroyAPIView):
    queryset = Wars.objects.all()
    serializer_class = WarsSerializer
    permission_classes = [AllowAny]


class WarsUpdateViewSet(UpdateAPIView):
    queryset = Wars.objects.all()
    serializer_class = WarsCreateSerializer
    permission_classes = [AllowAny]


class WarsDetailViewSet(RetrieveAPIView):
    queryset = Wars.objects.all()
    serializer_class = WarsSerializer
    permission_classes = [AllowAny]


class IsStartedFilter(ListAPIView):
    queryset = Wars.objects.filter(is_started=False)
    serializer_class = WarsSerializer
    permission_classes = [AllowAny]


class WarUsersCreateViewSet(CreateAPIView):
    queryset = WarUsers.objects.all()
    serializer_class = WarUsersCreateSerializer
    permission_classes = [AllowAny]


class WarUsersDeleteViewSet(DestroyAPIView):
    queryset = WarUsers.objects.all()
    serializer_class = WarUsersSerializer
    permission_classes = [AllowAny]


class WarUsersUpdateViewSet(UpdateAPIView):
    queryset = Wars.objects.all()
    serializer_class = WarUsersCreateSerializer
    permission_classes = [AllowAny]


class WarUsersDetailViewSet(RetrieveAPIView):
    queryset = WarUsers.objects.all()
    serializer_class = WarUsersSerializer
    permission_classes = [AllowAny]
