from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Ordine
from clienti.models import Cliente

from .serializers.ordini_serializers import OrdineSerializer


#crea gli ordini e li  mostra tutti

class OrdiniListCreateView(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Ordine.objects.all().order_by('numero_ordine')
    serializer_class = OrdineSerializer

#mostra gli ordini di un cliente 
class OrdiniListView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = OrdineSerializer

    def get_queryset(self):
        # Ottieni l'ID del cliente dalla richiesta
        cliente_id = self.kwargs.get('cliente_id')

        # Filtra gli ordini associati al cliente specifico
        queryset = Ordine.objects.filter(cliente_id=cliente_id).order_by('cognome')
        return queryset

#mostra un singolo ordine
class OrdiniDetailView(generics.RetrieveAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Ordine.objects.all()
    serializer_class = OrdineSerializer
    
#dato un cliente devo trovare quanti quanti e che tipo di ordine ha fatto
class NumeroOrdiniClienteView(generics.RetrieveAPIView):
    
    queryset = Cliente.objects.all()
    lookup_field = 'id'  # Campo utilizzato per recuperare l'oggetto
    
    def retrieve(self, request, *args, **kwargs):
        cliente = self.get_object()
        numero_ordini = Ordine.objects.filter(cliente=cliente).count()
        if numero_ordini == 0:
            return Response({'ordini': 'nessuno'})
        elif numero_ordini == 1:
            ordine= get_object_or_404(Ordine, cliente=cliente)
            tipo_ordine = ordine.programma.gruppo.nome_gruppo
            if tipo_ordine == 'Test':
                return Response({'ordini': 'solo_test'})
            else:
                 return Response({'ordini': 'completo'})
        else:
            return Response({'ordini': 'maggiore_due'})
        