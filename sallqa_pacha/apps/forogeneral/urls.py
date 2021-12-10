from django.urls import path
from .import views
app_name = 'app_nameforogeneral'

urlpatterns = [
    path('forogeneral/', views.Foro_General, name = 'boton_forogeneral')
    
]