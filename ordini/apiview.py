from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from dateutil.relativedelta import relativedelta

from django.shortcuts import get_object_or_404
from django.db.models import Prefetch

from .models import Ordine, AccordoNumero, Pagamento, Rate
from clienti.models import Cliente
from listini.models import Programmi
from utente.models import AnagraficaUtente

from .serializers.ordini_serializers import OrdineSerializer, OrdineRataSerializer, OrdineinfoSerializer
from clienti.serializers.cliente_serializers import ClientiSerializer
from utente.serializers.utente_serializers import UtenteSerializer
import pdb

# crea gli ordini e li  mostra tutti


class OrdiniListCreateView(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Ordine.objects.all()
    serializer_class = OrdineRataSerializer

    def perform_create(self, serializer):
        # Puoi eseguire operazioni personalizzate qui prima di creare l'oggetto
        # Ad esempio, puoi aggiungere campi extra prima di salvare l'oggetto

        numero_accordo = AccordoNumero()
        numero_accordo.tipo_accordo = 'ordine'
        numero_accordo.save()
        serializer.save(numero_ordine=numero_accordo)

        importo_ordine = serializer.instance.programma.importo
        pagamento = serializer.instance.programma.programma_rateale

        if pagamento:
            tipo_pagamento = 'Rateale'
        else:
            tipo_pagamento = 'Unica Soluzione'

        # creazione Pagamento
        pagamento = Pagamento(ordine=serializer.instance, importo=importo_ordine,
                              tipo_pagamento=tipo_pagamento, stato_ordine='Non Pagato')
        pagamento.save()

        if self.request.data.get('acconto') != 'False':

            numero_rate = int(self.request.data.get('numero_rate'))
            importo_acconto = int(self.request.data.get('acconto'))
            data_scadenza_rata = serializer.instance.data_ordine

            acconto = Rate(pagamento=pagamento, numero_rata=0,
                           importo_rata=importo_acconto, data_scadenza_rata=data_scadenza_rata)
            acconto.save()
            importo_rata = round(
                (float(importo_ordine) - float(importo_acconto)) / float(numero_rate), 3)
            for i in range(numero_rate):
                mesi = i + 2
                data_scadenza_nuova = data_scadenza_rata + \
                    relativedelta(months=mesi)

                rata = Rate(pagamento=pagamento, numero_rata=i+1,
                            importo_rata=importo_rata, data_scadenza_rata=data_scadenza_nuova)
                rata.save()


# mostra gli ordini di un cliente


class OrdiniListView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = OrdineSerializer

    def get_queryset(self):
        # Ottieni l'ID del cliente dalla richiesta
        cliente_id = self.kwargs.get('cliente_id')

        # Filtra gli ordini associati al cliente specifico
        queryset = Ordine.objects.filter(
            cliente_id=cliente_id)
        return queryset

 # mostra ultimo ordine di un cliente di un cliente


class OrdineUltimoView(generics.RetrieveAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Ordine.objects.all()
    serializer_class = OrdineSerializer
    lookup_field = 'cliente_id'

    def get_object(self):
        # Ottieni il valore dell'ID del cliente dalla richiesta
        cliente_id = self.kwargs.get('cliente_id')

        # Filtra gli ordini associati al cliente specifico e prendi l'ultimo
        queryset = self.get_queryset()
        obj = queryset.filter(cliente_id=cliente_id).last()

        if obj is None:
            raise NotFound("Nessun ordine trovato per questo cliente")

        return obj

# mostra un singolo ordine


class OrdiniDetailView(generics.RetrieveAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Ordine.objects.all()
    serializer_class = OrdineSerializer

# dato un cliente devo trovare quanti quanti e che tipo di ordine ha fatto


class NumeroOrdiniClienteView(generics.RetrieveAPIView):

    queryset = Cliente.objects.all()
    lookup_field = 'id'  # Campo utilizzato per recuperare l'oggetto

    def retrieve(self, request, *args, **kwargs):
        cliente = self.get_object()
        numero_ordini = Ordine.objects.filter(cliente=cliente).count()
        if numero_ordini == 0:
            return Response({'ordini': 'nessuno'})
        elif numero_ordini == 1:
            ordine = get_object_or_404(Ordine, cliente=cliente)
            tipo_ordine = ordine.programma.gruppo.nome_gruppo
            if tipo_ordine == 'Test':
                return Response({'ordini': 'solo_test'})
            else:
                return Response({'ordini': 'completo'})
        else:
            return Response({'ordini': 'maggiore_due'})


class DettagliOrdineView(generics.RetrieveAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Ordine.objects.all()
    serializer_class = OrdineSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        programma = instance.programma
        pagamento = get_object_or_404(Pagamento, ordine=instance)
        if pagamento.tipo_pagamento == 'Rateale':
            rate = Rate.objects.filter(pagamento=pagamento)
            importo_acconto = rate[0]['importo_rata']
            numero_rate = (rate.count()-1)
            importo_rate = rate[1]['importo_rata']

        else:
            importo_acconto = 0
            numero_rate = 0
            importo_rate = 0

        data = {
            'nome_programma': programma.nome_programma,
            'durata_programma': programma.durata_programma,
            'importo_programma': programma.importo,
            'tipo': pagamento.tipo_pagamento,
            'importo_acconto': importo_acconto,
            'numero_rate': numero_rate,
            'importo_rate': importo_rate
        }

        return Response(data)

# dati per la compilazione del modulo Informazioni


class CompilazioneModuloClienteOrdineView(generics.RetrieveAPIView):

    queryset = Cliente.objects.all()
    lookup_field = 'id'  # Campo utilizzato per recuperare l'oggetto

    def retrieve(self, request, *args, **kwargs):
        cliente = self.get_object()
        cliente_serializer = ClientiSerializer(cliente)
        cliente_json = cliente_serializer.data

        consulente_serializer = UtenteSerializer(cliente.consulente)
        consulente_json = consulente_serializer.data

        ordine = Ordine.objects.filter(cliente=cliente).last()
        ordine_serializer = OrdineSerializer(ordine)
        ordine_json = ordine_serializer.data

        programma = ordine.programma
        pagamento = get_object_or_404(Pagamento, ordine=ordine)
        if pagamento.tipo_pagamento == 'Rateale':
            rate = Rate.objects.filter(pagamento=pagamento)
            importo_acconto = rate[0].importo_rata
            numero_rate = (rate.count()-1)
            importo_rate = rate[1].importo_rata

        else:
            importo_acconto = 0
            numero_rate = 0
            importo_rate = 0

        data = {
            'cliente': cliente_json,
            'ordine': ordine_json,
            'consulente': consulente_json,
            'nome_programma': programma.nome_programma,
            'durata_programma': programma.durata_programma,
            'importo_programma': programma.importo,
            'tipo': pagamento.tipo_pagamento,
            'importo_acconto': importo_acconto,
            'numero_rate': numero_rate,
            'importo_rate': importo_rate,
            'numero_ordine': ordine.numero_ordine.numero_accordo
        }

        return Response(data)


class ListaOrdiniView(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = OrdineinfoSerializer
    queryset = Ordine.objects.all()
    lookup_field = 'consulente_id'
