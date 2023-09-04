from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Cliente, PersonalCheckUpCliente
from .serializers.cliente_serializers import ClientiSerializer
from .serializers.misure_serializers import MisureClientiSerializer




class ClienteListCreateView(generics.ListCreateAPIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Cliente.objects.all().order_by('cognome')
    serializer_class = ClientiSerializer
    
    def create(self, validated_data):
        instance = super().create(validated_data)
        return instance
    

class ClienteRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Cliente.objects.all()
    serializer_class = ClientiSerializer
    lookup_field = 'id'  # Campo utilizzato per recuperare l'oggetto 


class InserisciMisuraClienteAPIView(generics.CreateAPIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = PersonalCheckUpCliente.objects.all()
    serializer_class = MisureClientiSerializer

