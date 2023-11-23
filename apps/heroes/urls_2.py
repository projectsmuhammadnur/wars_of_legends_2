from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.heroes.views import UserHeroesCreateViewSet, UserHeroesDetailViewSet, UserHeroesUpdateViewSet, \
    UserHeroesDeleteViewSet

router = DefaultRouter()

urlpatterns = [
                  path('create/', UserHeroesCreateViewSet.as_view(),
                       name='user-heroes-detail'),
                  path('detail/<int:pk>/', UserHeroesDetailViewSet.as_view(),
                       name='user-heroes-detail'),
                  path('update/<int:pk>/', UserHeroesUpdateViewSet.as_view(),
                       name='user-heroes-detail'),
                  path('delete/<int:pk>/', UserHeroesDeleteViewSet.as_view(),
                       name='user-heroes-detail')
              ] + router.urls
