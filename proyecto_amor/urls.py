from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('dedicacion.urls')),  # URL principal vacía
    path('secretos/', include('dedicacion.urls')),  # También mantener esta por si acaso
]

# Solo en desarrollo (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)