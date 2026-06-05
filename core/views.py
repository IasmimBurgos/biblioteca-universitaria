from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Autor, Livro, Aluno, Emprestimo
from .serializers import (
    AutorSerializer,
    LivroSerializer,
    AlunoSerializer,
    EmprestimoSerializer
)


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all().order_by('-data_emprestimo')
    serializer_class = EmprestimoSerializer

    @action(detail=False, methods=['post'])
    def devolver(self, request):
        cpf = request.data.get('cpf')
        nome = request.data.get('nome')
        livro_id = request.data.get('livro_id')

        if not livro_id:
            return Response(
                {'erro': 'Informe o livro.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not cpf and not nome:
            return Response(
                {'erro': 'Informe o CPF ou o nome do aluno.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        emprestimos = Emprestimo.objects.filter(
            livro_id=livro_id,
            data_devolucao__isnull=True
        )

        if cpf:
            emprestimos = emprestimos.filter(aluno__cpf=cpf)

        if nome:
            emprestimos = emprestimos.filter(aluno__nome__iexact=nome)

        emprestimo = emprestimos.first()

        if not emprestimo:
            return Response(
                {'erro': 'Empréstimo ativo não encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )

        emprestimo.data_devolucao = timezone.now()
        emprestimo.save()

        livro = emprestimo.livro
        livro.estoque += 1
        livro.save()

        return Response(
            {'mensagem': 'Livro devolvido com sucesso!'},
            status=status.HTTP_200_OK
        )