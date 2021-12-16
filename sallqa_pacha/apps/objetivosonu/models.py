
from django.db import models
from django.db.models.fields import Field
from ..registrar.forms import CustomUserCreationForm
from ..iniciarsesion.models import Usuario
from django.shortcuts import reverse


class User(Usuario):
    pass

    def str__(self):
        return self.username

# Create your models here.
class Ods(models.Model):
    nombre = models.CharField(max_length= 30, null= False)
    imagen = models.ImageField(upload_to = 'imagenes_ods')
    descripcion = models.CharField(max_length= 300, null= False)


    def __str__(self):
        return self.nombre


class post(models.Model):
    nombre = models.CharField(max_length= 30, null= False)
    descripcion = models.CharField(max_length= 40, null= False)
    ods = models.ForeignKey(Ods, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=False, auto_now_add=True)
    titulo = models.CharField(max_length= 30, null= False)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to = 'imagenes_post')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            "slug": self.slug
        })

    def get_like_url(self):
        return reverse("like", kwargs={
            "slug": self.slug
        })

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()

    @property
    def get_view_count(self):
        return self.postview_set.all().count()

    @property
    def get_like_count(self):
        return self.like_set.all().count()

class comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.usename



class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
#class posteo(post):

#   nombre = post.nombre
#   descripcion = post.descripcion
#    fecha = post.fecha
#    titulo = post.titulo
#    cuerpo = post.cuerpo
#    imagen = post.imagen

#    def __str__(self):
#        return self.nombre
