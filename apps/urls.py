from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('telegram-users/', include('apps.telegram_users.urls')),
                  path('user-to-users/', include('apps.telegram_users.urls_2')),
                  path('heroes/', include('apps.heroes.urls')),
                  path('user-heroes/', include('apps.heroes.urls_2')),
                  path('medals/', include('apps.medals.urls')),
                  path('user-medals/', include('apps.medals.urls_2')),
                  path('war-user/', include('apps.war_user.urls')),
                  path('wars/', include('apps.wars.urls')),
                  path('war-users/', include('apps.wars.urls_2')),
                  path('equipments/', include('apps.equipments.urls')),
                  path('user-equipments/', include('apps.equipments.urls_2')),
                  path('donates/', include('apps.donates.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
