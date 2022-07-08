from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated
from blog.models import Usuario,Publicacao
from blog.serializers import UsuarioSerializer,PublicacaoSerializer  

class UsuariosViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated,)
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class ListaUsuarios(generics.ListAPIView):
    permission_classes =(IsAuthenticated,) 
    def queryset(self):
        queryset = Usuario.objects.all()
        return queryset
    serializer_class = UsuarioSerializer

class PublicacaoViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthenticated,)
    """Exibindo as publicações"""
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer
    