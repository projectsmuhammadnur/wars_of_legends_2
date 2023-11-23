from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.medals.views import MedalsCreateViewSet, MedalsUpdateViewSet, MedalsDeleteViewSet, MedalsDetailViewSet, \
    MedalsListViewSet

router = DefaultRouter()

urlpatterns = [
                  path('', MedalsListViewSet.as_view(),
                       name='medals-list'),
                  path('create/', MedalsCreateViewSet.as_view(),
                       name='medals-detail'),
                  path('detail/<int:pk>/', MedalsDetailViewSet.as_view(),
                       name='medals-detail'),
                  path('update/<int:pk>/', MedalsUpdateViewSet.as_view(),
                       name='medals-detail'),
                  path('delete/<int:pk>/', MedalsDeleteViewSet.as_view(),
                       name='medals-detail')
              ] + router.urls
