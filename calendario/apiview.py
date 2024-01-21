import pdb
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Appuntamento

from .serializers.calendario_serializers import AppuntamentoSerializer


class AppuntamentoListCreateView(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Appuntamento.objects.all()
    serializer_class = AppuntamentoSerializer



# recupera il cliente in base all'id, lo puo modificare


class AppuntamentoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Appuntamento.objects.all()
    serializer_class = AppuntamentoSerializer
    lookup_field = 'id'  # Campo utilizzato per recuperare l'oggetto

# crea un oggetto misure per il cliente

class AppuntamentoDestroyAPIView(generics.DestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Appuntamento.objects.all()
    serializer_class = AppuntamentoSerializer
    lookup_field = 'id'  # Campo utilizzato per recuperare l'oggetto

