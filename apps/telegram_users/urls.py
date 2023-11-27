from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.telegram_users.views import TelegramUsersDetailViewSet, TelegramUsersChatIdDetailViewSet, \
    TelegramUsersUpdateViewSet, TelegramUsersDeleteViewSet, TelegramUsersCreateViewSet, TelegramUsersListViewSet

router = DefaultRouter()

urlpatterns = [
                  path('', TelegramUsersListViewSet.as_view(),
                       name='heroes-list'),
                  path('create/', TelegramUsersCreateViewSet.as_view(),
                       name='telegram-users-detail'),
                  path('chat_id/<str:chat_id>/', TelegramUsersChatIdDetailViewSet.as_view(),
                       name='telegram-users-detail'),
                  path('detail/<int:pk>/', TelegramUsersDetailViewSet.as_view(),
                       name='telegram-users-detail'),
                  path('update/<int:pk>/', TelegramUsersUpdateViewSet.as_view(),
                       name='telegram-users-detail'),
                  path('delete/<int:pk>/', TelegramUsersDeleteViewSet.as_view(),
                       name='telegram-users-detail')
              ] + router.urls
