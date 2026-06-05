from django.contrib import admin
from .models import Autor, Livro, Pedido

admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Pedido)
