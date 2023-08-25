from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Cliente
from .serializers.cliente_serializers import ClientiSerializer, ClienteSerializer



class ClienteListCreateView(generics.ListCreateAPIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Cliente.objects.all().order_by('cognome')
    serializer_class = ClientiSerializer
    

class ClienteRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    lookup_field = 'id'  # Campo utilizzato per recuperare l'oggetto 
    