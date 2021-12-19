
from django.shortcuts import render
from .models import Ods, Post, Comment
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import formulario_altapost, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AltaPost(LoginRequiredMixin, CreateView):
    model = 'post'
    template_name = 'objetivosonu/altapost.html'
    form_class = formulario_altapost
    success_url = reverse_lazy('inicio')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
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
    p = Post.objects.filter(ods = ods)
    ctx = {}
    ctx['p'] = p
    
    return render(request, 'objetivosonu/posts.html', ctx)

def posteo(request, pk):
    
    post = Post.objects.get(pk = pk)
    ctx = {}
    ctx['post'] = post


    return render(request, 'objetivosonu/posteo.html', ctx)




    