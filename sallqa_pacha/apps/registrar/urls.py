from django.urls import path
from .import views
app_name = 'app_registrar'

urlpatterns = [
    path('registro/', views.regitrar_User, name = 'boton_registrar')
    
]