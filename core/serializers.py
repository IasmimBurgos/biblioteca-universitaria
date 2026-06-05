from rest_framework import serializers
from .models import Autor, Livro, Pedido


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor


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
        extra_kwargs = {
            'autor': {'required': False}  
        }

    def create(self, validated_data):
        autor_nome = validated_data.pop('autor_nome')
        autor_obj, _ = Autor.objects.get_or_create(nome=autor_nome)

        return Livro.objects.create(autor=autor_obj, **validated_data)
    
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'