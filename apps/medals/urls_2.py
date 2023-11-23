from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.medals.views import UserMedalsCreateViewSet, UserMedalsDetailViewSet, UserMedalsUpdateViewSet, \
    UserMedalsDeleteViewSet

router = DefaultRouter()

urlpatterns = [
                  path('create/', UserMedalsCreateViewSet.as_view(),
                       name='user-medals-detail'),
                  path('detail/<int:pk>/', UserMedalsDetailViewSet.as_view(),
                       name='user-medals-detail'),
                  path('update/<int:pk>/', UserMedalsUpdateViewSet.as_view(),
                       name='user-medals-detail'),
                  path('delete/<int:pk>/', UserMedalsDeleteViewSet.as_view(),
                       name='user-medals-detail')
              ] + router.urls
