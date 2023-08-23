from rest_framework import generics
from .models import Cliente
from .serializers.cliente_serializers import ClienteSerializer



class ClienteListCreateView(generics.ListCreateAPIView):
    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer