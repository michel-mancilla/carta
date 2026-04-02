# dedicacion/urls.py (Versión Corregida)

from django.urls import path
from . import views

urlpatterns = [
    # 🌟 CORRECCIÓN CRÍTICA: La ruta raíz (la primera línea) debe apuntar a la vista que SÍ existe.
    path('', views.inicio, name='inicio'), # Usa views.inicio, que es tu vista principal real.
    # Rutas secundarias (Asegúrate de que estas vistas existan en views.py)
    path('carta/', views.carta_secreta, name='carta'),
    path('recuerdos/', views.nuestros_recuerdos, name='recuerdos'),
    path('amor/', views.mi_amor, name='amor'),
    path('palabras/', views.palabras_especiales, name='palabras'),
    path('aniversario/', views.mensaje_aniversario, name='aniversario'),
]