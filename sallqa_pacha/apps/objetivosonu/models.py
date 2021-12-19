from django.db import models
from django.db.models.fields import Field
from ..registrar.forms import CustomUserCreationForm
from ..iniciarsesion.models import Usuario
from django.shortcuts import reverse
from django.contrib.contenttypes.models import ContentType


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


class Post(models.Model):
    nombre = models.CharField(max_length= 30, null= False)
    descripcion = models.CharField(max_length= 40, null= False)
    ods = models.ForeignKey(Ods, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=False, auto_now_add=True)
    titulo = models.CharField(max_length= 30, null= False)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to = 'imagenes_post')

    def __str__(self):
        return self.nombre

class Comment(models.Model):
    post = models.ForeignKey(Post , blank=True, null=True,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

