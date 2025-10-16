from django.contrib import admin

# Register your models here.
from .models import Editora, Autor, Livro, Publica

admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Publica)