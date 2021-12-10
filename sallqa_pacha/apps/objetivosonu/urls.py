from django.urls import path
from .import views
app_name = 'app_objetivosonu'

urlpatterns = [
    path('objetivos/', views.objetivos_ONU, name = 'boton_objetivosONU')
    
]