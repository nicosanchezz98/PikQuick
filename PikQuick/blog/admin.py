from django.contrib import admin

# Register your models here.
from blog.models import User, Post, Coment

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Coment)
