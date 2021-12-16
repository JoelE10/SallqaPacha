from django import forms
from django.forms import fields
from .models import post

class formulario_altapost(forms.ModelForm):
    class Meta:
        model = post
        fields = '__all__'