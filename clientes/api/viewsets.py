from rest_framework.viewsets import ModelViewSet
from clientes.models import Tipo
from clientes.api.serializers import TipoSerializer
from rest_framework import generics, permissions

class TipoViewSet(ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer
    permission_classes = (permissions.IsAuthenticated,)
