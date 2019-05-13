from rest_framework.serializers import ModelSerializer
from clientes.models import Tipo

class TipoSerializer(ModelSerializer):
    class Meta:
        model = Tipo
        fields = (
            'id',
            'nome',
            'descricao'
        )