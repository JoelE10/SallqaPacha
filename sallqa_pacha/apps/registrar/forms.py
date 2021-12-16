# Create your models here.
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import get_user_model
#User = get_user_model()
from ..iniciarsesion.models import Usuario


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', ]