from django.db import models
import uuid

class Autor(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Autores"


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, related_name='livros', on_delete=models.CASCADE)
    estoque = models.IntegerField()
    descricao = models.TextField()

    capa_do_livro = models.ImageField(upload_to='capas/', blank=True, null=True)

    data_publicacao = models.DateField()
    paginas = models.IntegerField()

    genero = models.CharField(max_length=255)

    @property
    def status(self):
        if self.estoque > 0:
            return "Disponível"
        return "Alugado"

    def __str__(self):
        return self.titulo


class Pedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    pais = models.CharField(max_length=100)
    quantidade = models.IntegerField()

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.livro.titulo}"