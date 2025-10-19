from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carta/', views.carta_secreta, name='carta'),
    path('recuerdos/', views.nuestros_recuerdos, name='recuerdos'),
    path('amor/', views.mi_amor, name='amor'),
    path('palabras/', views.palabras_especiales, name='palabras'),
    path('', views.inicio, name='inicio'),
]