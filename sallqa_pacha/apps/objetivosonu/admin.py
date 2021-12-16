from django.contrib import admin

from .models import Ods, post, comentario, Like, PostView

admin.site.register(Ods)
admin.site.register(post)
admin.site.register(comentario)
admin.site.register(Like)
admin.site.register(PostView)
