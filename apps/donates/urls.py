from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.donates.views import DonatesCreateViewSet, DonatesUpdateViewSet, DonatesDeleteViewSet, \
    DonatesDetailViewSet, DonatesListViewSet

router = DefaultRouter()

urlpatterns = [
                  path('', DonatesListViewSet.as_view(),
                       name='donates-list'),
                  path('create/', DonatesCreateViewSet.as_view(),
                       name='donates-create'),
                  path('detail/<int:pk>/', DonatesDetailViewSet.as_view(),
                       name='donates-detail'),
                  path('update/<int:pk>/', DonatesUpdateViewSet.as_view(),
                       name='donates-update'),
                  path('delete/<int:pk>/', DonatesDeleteViewSet.as_view(),
                       name='donates-delete')
              ] + router.urls
