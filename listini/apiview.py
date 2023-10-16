from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .serializers.gruppolistinoserializers import GruppoListinoSerializer
from .serializers.programmiserializers import ProgrammiSerializer

from .models import GruppoListino, Programmi
from consulenti.models import Struttura
from ordini.models import Ordine


class GruppoListinoListView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = GruppoListinoSerializer

    def get_queryset(self):

        eta = self.request.data.get('minorenne')
        gruppi_visibili = self.request.data.get('gruppi_visibili')
        listino = get_object_or_404(Struttura, nome='Centro Autorizzato')

        if gruppi_visibili == 'primo_ordine':
            gruppi = GruppoListino.objects.filter(visibilta_primo_ordine=True)

        programmi_validi = Programmi.objects.filter(
            programma_kids=eta, programma_attivo=True, listino_dedicato=listino, gruppo__in=gruppi)

        valori_unici = programmi_validi.values_list(
            'gruppo', flat=True).distinct()

        queryset = GruppoListino.objects.filter(id__in=valori_unici)
        return queryset


class ProgrammiListView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProgrammiSerializer

    def get_queryset(self):

        listino = get_object_or_404(Struttura, nome='Centro Autorizzato')
        id = self.request.query_params.get('id')
        minore = self.request.query_params.get('minore')
        pagamento = self.request.query_params.get('pagamento')
        cliente_id = self.request.query_params.get('cliente_id')

        ordini = Ordine.objects.filter(cliente=cliente_id)

        if ordini.exists():
            queryset = Programmi.objects.filter(
                programma_kids=minore, programma_attivo=True,
                programma_rateale=pagamento, programma_proseguimento=True, listino_dedicato=listino, gruppo_id=id)

        else:
            queryset = Programmi.objects.filter(
                programma_kids=minore, programma_attivo=True,
                programma_rateale=pagamento, programma_proseguimento=False, listino_dedicato=listino, gruppo_id=id)
        return queryset


class GruppoBoolView(generics.RetrieveAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = GruppoListinoSerializer
    # Sostituisci con il queryset del tuo modello
    queryset = GruppoListino.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if Programmi.objects.filter(gruppo=instance, programma_rateale=True).exists():
            rateale = True
        else:
            rateale = False

        if Programmi.objects.filter(gruppo=instance, programma_rateale=False).exists():
            unico = True
        else:
            unico = False

        data = {
            'unico': unico,
            'rateale': rateale,
        }

        return Response(data)
