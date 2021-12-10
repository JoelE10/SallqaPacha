from django.urls import path
from .import views
app_name = 'app_iniciodesesion'

urlpatterns = [
    path('iniciodesesion/', views.inicio_De_Sesion, name = 'boton_iniciodesesion')
    
]