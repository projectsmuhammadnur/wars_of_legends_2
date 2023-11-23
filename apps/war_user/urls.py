from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.war_user.views import WarUserDetailViewSet, WarUserUpdateViewSet, WarUserDeleteViewSet, \
    WarUserCreateViewSet

router = DefaultRouter()

urlpatterns = [
                  path('create/', WarUserCreateViewSet.as_view(),
                       name='war-user-detail'),
                  path('detail/<int:pk>/', WarUserDetailViewSet.as_view(),
                       name='war-user-detail'),
                  path('update/<int:pk>/', WarUserUpdateViewSet.as_view(),
                       name='war-user-detail'),
                  path('delete/<int:pk>/', WarUserDeleteViewSet.as_view(),
                       name='war-user-detail')
              ] + router.urls
