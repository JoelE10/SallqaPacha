from django.shortcuts import render

# Create your views here.

def acercaDe(request):
    return render (request,'acercade/ACERCA_DE.html' )