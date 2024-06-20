from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from src.utils.enums import Environment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<str:version>/vacancies/', include('src.apps.vacancy.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    if settings.DJANGO_ENVIRONMENT == Environment.DEV.value:
        from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

        urlpatterns += [
            path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
            path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
            path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
        ]
