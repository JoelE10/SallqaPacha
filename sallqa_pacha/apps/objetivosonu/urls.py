from django.urls import path
from .import views
app_name = 'app_objetivosonu'

urlpatterns = [
    path('objetivos/', views.objetivos_ONU, name = 'boton_objetivosONU'),
    
    path('posts/<int:pk>', views.posts, name='posts'),
    #path('posts/', views.posts, name='posts')

    path('posteo/<int:pk>', views.posteo, name='posteo'),
    path('altapost/', views.AltaPost.as_view(), name="altapost")
]