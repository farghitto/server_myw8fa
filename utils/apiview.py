from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from datetime import datetime

from .serializers.stato_bmi_serializers import statoPesoSerializer

from clienti.models import Cliente
from .models import StatoPeso, Bmiottimale

# authentication_classes = [TokenAuthentication]
# permission_classes = [IsAuthenticated]


class StatoBmi(generics.RetrieveAPIView):
    queryset = Bmiottimale.objects.all()
    serializer_class = statoPesoSerializer

    def retrieve(self, request, id, bmi):
        cliente = get_object_or_404(Cliente, id=id)

        stati = StatoPeso.objects.filter(sesso=cliente.sesso)
        for stato in stati:
            
            if float(bmi) <= float(stato.bmi):
                stato_attuale = stato.qualitapeso
                break
            else:
                stato_attuale = stato.qualitapeso
                

        return Response(stato_attuale)
