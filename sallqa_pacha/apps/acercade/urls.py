from django.urls import path
from .import views
app_name = 'app_acercade'

urlpatterns = [
    path('datosacercade/', views.acercaDe, name = 'boton_acercade')
    
]