from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.telegram_users.views import UserToUsersDetailViewSet, UserToUsersUpdateViewSet, UserToUsersDeleteViewSet, \
    UserToUsersCreateViewSet

router = DefaultRouter()

urlpatterns = [
                  path('create/', UserToUsersCreateViewSet.as_view(),
                       name='user-to-users-detail'),
                  path('detail/<int:pk>/', UserToUsersDetailViewSet.as_view(),
                       name='user-to-users-detail'),
                  path('update/<int:pk>/', UserToUsersUpdateViewSet.as_view(),
                       name='user-to-users-detail'),
                  path('delete/<int:pk>/', UserToUsersDeleteViewSet.as_view(),
                       name='user-to-users-detail')
              ] + router.urls
