from django.contrib import admin

from .models import Ods, Post, PostView, Comment

admin.site.register(Ods)
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)
