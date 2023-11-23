from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from apps.medals.models import Medals, UserMedals
from apps.medals.serializers import MedalsCreateSerializer, MedalsSerializer, UserMedalsSerializer, \
    UserMedalsCreateSerializer


class MedalsListViewSet(ListAPIView):
    queryset = Medals.objects.all()
    serializer_class = MedalsSerializer


class MedalsCreateViewSet(CreateAPIView):
    queryset = Medals.objects.all()
    serializer_class = MedalsCreateSerializer
    permission_classes = [AllowAny]


class MedalsDeleteViewSet(DestroyAPIView):
    queryset = Medals.objects.all()
    serializer_class = MedalsSerializer
    permission_classes = [AllowAny]


class MedalsUpdateViewSet(UpdateAPIView):
    queryset = Medals.objects.all()
    serializer_class = MedalsCreateSerializer
    permission_classes = [AllowAny]


class MedalsDetailViewSet(RetrieveAPIView):
    queryset = Medals.objects.all()
    serializer_class = MedalsSerializer
    permission_classes = [AllowAny]


class UserMedalsCreateViewSet(CreateAPIView):
    queryset = UserMedals.objects.all()
    serializer_class = UserMedalsCreateSerializer
    permission_classes = [AllowAny]


class UserMedalsDeleteViewSet(DestroyAPIView):
    queryset = UserMedals.objects.all()
    serializer_class = UserMedalsSerializer
    permission_classes = [AllowAny]


class UserMedalsUpdateViewSet(UpdateAPIView):
    queryset = Medals.objects.all()
    serializer_class = UserMedalsCreateSerializer
    permission_classes = [AllowAny]


class UserMedalsDetailViewSet(RetrieveAPIView):
    queryset = UserMedals.objects.all()
    serializer_class = UserMedalsSerializer
    permission_classes = [AllowAny]
