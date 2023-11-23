from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.heroes.views import HeroesCreateViewSet, HeroesUpdateViewSet, HeroesDeleteViewSet, HeroesDetailViewSet, \
    HeroesListViewSet

router = DefaultRouter()

urlpatterns = [
                  path('', HeroesListViewSet.as_view(),
                       name='heroes-list'),
                  path('create/', HeroesCreateViewSet.as_view(),
                       name='heroes-detail'),
                  path('detail/<int:pk>/', HeroesDetailViewSet.as_view(),
                       name='heroes-detail'),
                  path('update/<int:pk>/', HeroesUpdateViewSet.as_view(),
                       name='heroes-detail'),
                  path('delete/<int:pk>/', HeroesDeleteViewSet.as_view(),
                       name='heroes-detail')
              ] + router.urls
