
from django.shortcuts import render
from .models import Ods, post
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import formulario_altapost
from django.contrib.auth.mixins import LoginRequiredMixin


class AltaPost(LoginRequiredMixin, CreateView):
    model = 'post'
    template_name = 'objetivosonu/altapost.html'
    form_class = formulario_altapost
    success_url = reverse_lazy('inicio')
    

# Create your views here.

def objetivos_ONU(request):
    r = Ods.objects.all() 
    
    ctx = {}
    ctx['odss'] = r

    #ods = Ods.objects.filter(ods)
    #pi = post.objects.all()
    #ctx = {}
    #ctx['pi'] = pi
  

    return render (request,'objetivosonu/OBJETIVOSONU.html', ctx )



def posts(request, pk):
    ods = Ods.objects.get(pk = pk )
    p = post.objects.filter(ods = ods)
    ctx = {}
    ctx['p'] = p
    
    return render(request, 'objetivosonu/posts.html', ctx)

def posteo(request, pk):
    
    l = post.objects.get(pk = pk)
    ctx = {}
    ctx['l'] = l

    return render(request, 'objetivosonu/posteo.html', ctx)
    