from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.equipments.views import EquipmentsCreateViewSet, EquipmentsUpdateViewSet, EquipmentsDeleteViewSet, \
    EquipmentsDetailViewSet, EquipmentsListViewSet

router = DefaultRouter()

urlpatterns = [
                  path('', EquipmentsListViewSet.as_view(),
                       name='equipments-list'),
                  path('create/', EquipmentsCreateViewSet.as_view(),
                       name='equipments-detail'),
                  path('detail/<int:pk>/', EquipmentsDetailViewSet.as_view(),
                       name='equipments-detail'),
                  path('update/<int:pk>/', EquipmentsUpdateViewSet.as_view(),
                       name='equipments-detail'),
                  path('delete/<int:pk>/', EquipmentsDeleteViewSet.as_view(),
                       name='equipments-detail')
              ] + router.urls
