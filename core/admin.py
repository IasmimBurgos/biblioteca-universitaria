from django.contrib import admin
from .models import Autor, Livro, Aluno, Emprestimo

admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Aluno)
admin.site.register(Emprestimo)