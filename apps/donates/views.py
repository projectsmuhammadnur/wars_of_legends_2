from rest_framework.generics import UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from apps.donates.models import Donates
from apps.donates.serializers import DonatesSerializer, DonatesCreateSerializer


class DonatesListViewSet(ListAPIView):
    queryset = Donates.objects.all()
    serializer_class = DonatesSerializer
    permission_classes = [AllowAny]


class DonatesCreateViewSet(CreateAPIView):
    queryset = Donates.objects.all()
    serializer_class = DonatesCreateSerializer
    permission_classes = [AllowAny]


class DonatesDeleteViewSet(DestroyAPIView):
    queryset = Donates.objects.all()
    serializer_class = DonatesSerializer
    permission_classes = [AllowAny]


class DonatesUpdateViewSet(UpdateAPIView):
    queryset = Donates.objects.all()
    serializer_class = DonatesCreateSerializer
    permission_classes = [AllowAny]


class DonatesDetailViewSet(RetrieveAPIView):
    queryset = Donates.objects.all()
    serializer_class = DonatesSerializer
    permission_classes = [AllowAny]
