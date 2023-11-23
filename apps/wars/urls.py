from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.wars.views import WarsDeleteViewSet, WarsDetailViewSet, WarsUpdateViewSet, WarsCreateViewSet, IsStartedFilter

router = DefaultRouter()

urlpatterns = [
                  path('create/', WarsCreateViewSet.as_view(),
                       name='wars-detail'),
                  path('detail/<int:pk>/', WarsDetailViewSet.as_view(),
                       name='wars-detail'),
                  path('update/<int:pk>/', WarsUpdateViewSet.as_view(),
                       name='wars-detail'),
                  path('delete/<int:pk>/', WarsDeleteViewSet.as_view(),
                       name='wars-detail'),
                  path('filter/is_started/', IsStartedFilter.as_view(),
                       name='wars-filter'),
              ] + router.urls
