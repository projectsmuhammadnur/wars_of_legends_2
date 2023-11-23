from rest_framework.generics import UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from apps.equipments.models import Equipments, UserEquipments
from apps.equipments.serializers import EquipmentsSerializer, EquipmentsCreateSerializer, UserEquipmentsSerializer, \
    UserEquipmentsCreateSerializer


class EquipmentsListViewSet(ListAPIView):
    queryset = Equipments.objects.all()
    serializer_class = EquipmentsSerializer


class EquipmentsCreateViewSet(CreateAPIView):
    queryset = Equipments.objects.all()
    serializer_class = EquipmentsCreateSerializer
    permission_classes = [AllowAny]


class EquipmentsDeleteViewSet(DestroyAPIView):
    queryset = Equipments.objects.all()
    serializer_class = EquipmentsSerializer
    permission_classes = [AllowAny]


class EquipmentsUpdateViewSet(UpdateAPIView):
    queryset = Equipments.objects.all()
    serializer_class = EquipmentsCreateSerializer
    permission_classes = [AllowAny]


class EquipmentsDetailViewSet(RetrieveAPIView):
    queryset = Equipments.objects.all()
    serializer_class = EquipmentsSerializer
    permission_classes = [AllowAny]


class UserEquipmentsCreateViewSet(CreateAPIView):
    queryset = UserEquipments.objects.all()
    serializer_class = UserEquipmentsCreateSerializer
    permission_classes = [AllowAny]


class UserEquipmentsDeleteViewSet(DestroyAPIView):
    queryset = UserEquipments.objects.all()
    serializer_class = UserEquipmentsSerializer
    permission_classes = [AllowAny]


class UserEquipmentsUpdateViewSet(UpdateAPIView):
    queryset = UserEquipments.objects.all()
    serializer_class = UserEquipmentsCreateSerializer
    permission_classes = [AllowAny]


class UserEquipmentsDetailViewSet(RetrieveAPIView):
    queryset = UserEquipments.objects.all()
    serializer_class = UserEquipmentsSerializer
    permission_classes = [AllowAny]
