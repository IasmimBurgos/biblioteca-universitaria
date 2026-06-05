from rest_framework import serializers
from .models import Autor, Livro, Aluno, Emprestimo


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class LivroSerializer(serializers.ModelSerializer):
    autor_nome = serializers.CharField(write_only=True)
    nome_autor = serializers.ReadOnlyField(source='autor.nome')
    genero = serializers.CharField()
    status = serializers.ReadOnlyField()

    class Meta:
        model = Livro
        fields = [
            'id',
            'titulo',
            'autor_nome',
            'nome_autor',
            'estoque',
            'descricao',
            'capa_do_livro',
            'data_publicacao',
            'paginas',
            'genero',
            'status'
        ]

    def create(self, validated_data):
        autor_nome = validated_data.pop('autor_nome')
        autor_obj, _ = Autor.objects.get_or_create(
            nome=autor_nome.strip()
        )

        return Livro.objects.create(
            autor=autor_obj,
            **validated_data
        )


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'


class EmprestimoSerializer(serializers.ModelSerializer):

    livro_titulo = serializers.ReadOnlyField(source='livro.titulo')

    aluno_detalhes = AlunoSerializer(
        source='aluno',
        read_only=True
    )

    aluno_cpf = serializers.CharField(
        write_only=True,
        required=False,
        allow_blank=True
    )

    aluno_nome = serializers.CharField(
        write_only=True,
        required=False,
        allow_blank=True
    )

    class Meta:
        model = Emprestimo
        fields = [
            'id',
            'livro',
            'livro_titulo',
            'data_emprestimo',
            'data_devolucao',
            'aluno_detalhes',
            'aluno_cpf',
            'aluno_nome'
        ]

    def validate(self, data):
        cpf = data.get('aluno_cpf')
        nome = data.get('aluno_nome')

        if not cpf and not nome:
            raise serializers.ValidationError(
                'Informe o CPF ou o nome do aluno.'
            )

        return data

    def create(self, validated_data):
        cpf = validated_data.pop('aluno_cpf', '').strip()
        nome = validated_data.pop('aluno_nome', '').strip()

        livro = validated_data['livro']

        if livro.estoque <= 0:
            raise serializers.ValidationError(
                {'livro': 'Livro indisponível para empréstimo.'}
            )

        aluno = None

        if cpf:
            aluno = Aluno.objects.filter(cpf=cpf).first()

        if not aluno and nome:
            aluno = Aluno.objects.filter(nome__iexact=nome).first()

        if not aluno:
            raise serializers.ValidationError(
                {'aluno': 'Aluno não encontrado. Cadastre ou gere alunos primeiro.'}
            )

        livro.estoque -= 1
        livro.save()

        return Emprestimo.objects.create(
            livro=livro,
            aluno=aluno
        )