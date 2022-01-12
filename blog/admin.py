from django.contrib import admin
from .models import Post  # Usando el modelo de la tabla Post

admin.site.register(Post)  # Agrega la taba Post al Admin

