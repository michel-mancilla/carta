from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 1. Ruta de Administración de Django (admin/)
    path('admin/', admin.site.urls), 

    # 2. Inclusión de las URLs de tu aplicación principal ('dedicacion')
    # Esto asegura que todas las peticiones a la raíz del sitio (/) pasen a tu aplicación.
    path('', include('dedicacion.urls')), 
    
    # Si quieres la ruta /secretos/ también, la dejas aquí:
    path('secretos/', include('dedicacion.urls')), 
]

# **IMPORTANTE:** Esto solo debe estar activo cuando DEBUG=True (desarrollo local).
# En Vercel (producción), Whitenoise se encarga de los estáticos.
if settings.DEBUG:
    # Esta línea debe ser eliminada antes del despliegue final si no la usas.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # Esta línea es NECESARIA en desarrollo local, pero IGNORADA en Vercel.
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)