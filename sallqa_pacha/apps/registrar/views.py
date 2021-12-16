from django.shortcuts import redirect, render
from django import forms
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

    
def regitrar_User(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, 'registro exitoso')
            return redirect(to='inicio')
        data["form"] = formulario
    return render (request,'registrar/REGISTROS.html', data )

