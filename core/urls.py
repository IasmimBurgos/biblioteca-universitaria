from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, LivroViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'livros', LivroViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]