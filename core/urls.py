from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AutorViewSet,
    LivroViewSet,
    AlunoViewSet,
    EmprestimoViewSet
)

router = DefaultRouter()

router.register(r'autores', AutorViewSet)
router.register(r'livros', LivroViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'emprestimos', EmprestimoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]