from django.shortcuts import render

# Create your views here.

def inicio_De_Sesion(request):
    return render (request,'iniciosesion/INICIODESESION.html' )