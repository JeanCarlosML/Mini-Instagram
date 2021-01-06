from django.contrib import admin
from posts.models import Post
# Register your models here.

#Registramos el modelo Post en el dashboard de admin
admin.site.register(Post)