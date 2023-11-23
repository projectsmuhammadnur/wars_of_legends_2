from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.wars.views import WarUsersCreateViewSet, WarUsersDetailViewSet, WarUsersUpdateViewSet, WarUsersDeleteViewSet

router = DefaultRouter()

urlpatterns = [
                  path('create/', WarUsersCreateViewSet.as_view(),
                       name='war-users-detail'),
                  path('detail/<int:pk>/', WarUsersDetailViewSet.as_view(),
                       name='war-users-detail'),
                  path('update/<int:pk>/', WarUsersUpdateViewSet.as_view(),
                       name='war-users-detail'),
                  path('delete/<int:pk>/', WarUsersDeleteViewSet.as_view(),
                       name='war-users-detail')
              ] + router.urls
