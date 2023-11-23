from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.equipments.views import UserEquipmentsCreateViewSet, UserEquipmentsDetailViewSet, UserEquipmentsUpdateViewSet, \
    UserEquipmentsDeleteViewSet

router = DefaultRouter()

urlpatterns = [
                  path('create/', UserEquipmentsCreateViewSet.as_view(),
                       name='user-equipments-detail'),
                  path('detail/<int:pk>/', UserEquipmentsDetailViewSet.as_view(),
                       name='user-equipments-detail'),
                  path('update/<int:pk>/', UserEquipmentsUpdateViewSet.as_view(),
                       name='user-equipments-detail'),
                  path('delete/<int:pk>/', UserEquipmentsDeleteViewSet.as_view(),
                       name='user-equipments-detail')
              ] + router.urls
