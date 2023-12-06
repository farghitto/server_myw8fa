import pdb
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Alimenti, Cliente, PersonalCheckUpCliente, DatiModuloInformazioniClienti, StatoPeso, PatologieClienti, DatiModuloInformazioniClienti, GustiClienti
from utils.models import Bmiottimale
from utente.models import AnagraficaUtente
from ordini.models import Ordine
from django.contrib.auth.models import User


from .serializers.cliente_serializers import ClientiSerializer, StatoPesoSerializer, PatologieSerializer, AlimentiSerializer
from .serializers.misure_serializers import MisureClientiSerializer, CampiMisureSerializer, MisureClientiPesoSerializer
from .serializers.cliente_serializers import  InformazioniClientiSerializer, InformazioniClientiGustiSerializer, GustiClientiSerializer
from ordini.serializers.ordini_serializers import OrdineSerializer

# crea i clienti e ne restituisce la lista
class ClienteListCreateView(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Cliente.objects.all().order_by('cognome')
    serializer_class = ClientiSerializer

    def perform_create(self, serializer):
        # aggiunge il consulente per ora quello che sta accedendo al programma
        consulente = get_object_or_404(
            AnagraficaUtente, utente=self.request.user)
        serializer.save(consulente=consulente)

# recupera il cliente in base all'id, lo puo modificare


class ClienteRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Cliente.objects.all()
    serializer_class = ClientiSerializer
    lookup_field = 'id'  # Campo utilizzato per recuperare l'oggetto

# crea un oggetto misure per il cliente


class InserisciMisuraClienteAPIView(generics.CreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = PersonalCheckUpCliente.objects.all()
    serializer_class = MisureClientiSerializer

    def perform_create(self, serializer):

        cliente = get_object_or_404(Cliente, id=serializer.data['cliente'])
        bmi_ottimale = get_object_or_404(Bmiottimale, sesso=cliente.sesso)
        peso_ottimale = round(float(bmi_ottimale.valore)
                              * (pow((float(cliente.altezza)/100), 2)), 2)

        dati_validati = serializer.validated_data

        # Aggiungi il nuovo campo ai dati
        dati_validati['peso_ottimale'] = peso_ottimale

        # Crea un'istanza del modello con i dati modificati
        nuovo_oggetto = PersonalCheckUpCliente(**dati_validati)

        # Salva l'oggetto nel database
        nuovo_oggetto.save()


class MisuraClienteAPIView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = MisureClientiSerializer

    def get_queryset(self):
        id = self.kwargs['id']  # Ottieni l'ID dell'autore dalla URL
        return PersonalCheckUpCliente.objects.filter(cliente_id=id)


class CampiMisureAPI(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Sostituisci con il tuo serializzatore reale
    serializer_class = CampiMisureSerializer

    def get(self, request):
        # Ottenere i nomi dei campi del modello come una lista
        campi_modello = []

        for campo in PersonalCheckUpCliente._meta.get_fields():

            nome_campo = campo.name  # Nome del campo
            verbose_name = campo.verbose_name  # "Verbose name" del campo
            campi_modello.append((nome_campo, verbose_name))

        campi_da_escludere = ['cliente', 'data',
                              'ID', 'peso ottimale']

        # Filtra i campi rimuovendo quelli da escludere
        campi_filtrati = [
            campo for campo in campi_modello if campo[1] not in campi_da_escludere]

        return Response(campi_filtrati, status=status.HTTP_200_OK)


class MisuraClientePesoInizialeAPIView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = MisureClientiPesoSerializer

    def get(self, request,  id):

        peso = PersonalCheckUpCliente.objects.filter(cliente_id=id).first()
        if peso is not None:
            dati_ritorno = {"peso": str(peso.peso)}
        else:
            dati_ritorno = {"peso": 'Non disponibile'}

        return Response(dati_ritorno)


class NuovoClienteAPIView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = MisureClientiPesoSerializer

    def get(self, request,  id):

        risposte = PersonalCheckUpCliente.objects.filter(cliente_id=id).count()
        if risposte == 1:
            dati_ritorno = {"misure": 'True'}
        else:
            dati_ritorno = {"misure": 'False'}

        return Response(dati_ritorno)

# verifica che il cliente abbia il modulo informazioni compilato


class VerificaDatiCliente(generics.RetrieveAPIView):

    queryset = DatiModuloInformazioniClienti.objects.all()

    def retrieve(self, request, cliente_id):
        try:
            cliente = DatiModuloInformazioniClienti.objects.get(
                cliente_id=cliente_id)
            return Response({'esiste': True}, status=status.HTTP_200_OK)
        except DatiModuloInformazioniClienti.DoesNotExist:
            return Response({'esiste': False}, status=status.HTTP_200_OK)


class StatoPesoAPIView(generics.RetrieveAPIView):

    queryset = StatoPeso.objects.all()
    serializer_class = StatoPesoSerializer

    def retrieve(self, request):

        sesso = self.request.data.get('sesso')
        bmi = self.request.data.get('bmi')
        stati = StatoPeso.objects.filter(sesso=sesso)

        for stato in stati:

            if float(bmi) <= float(stato.bmi):

                stato_attuale = stato.qualitapeso
                break

        return Response(stato_attuale)


class PatologieListAPIView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = PatologieSerializer
    queryset = PatologieClienti.objects.all()


class AlimentiListAPIView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = AlimentiSerializer
    queryset = Alimenti.objects.all().order_by('classe_alimenti', 'nome')



class InformazioniClientiCreateAPIView(generics.CreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = InformazioniClientiSerializer
    queryset = DatiModuloInformazioniClienti.objects.all()


class InformazioniClientiGustiAPIView(generics.RetrieveAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = InformazioniClientiGustiSerializer
    queryset = DatiModuloInformazioniClienti.objects.all()
    lookup_field = 'cliente_id'
    

class ClientiGustiCreateAPIView(generics.CreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = GustiClientiSerializer
    queryset = GustiClienti.objects.all()
    

class CompilazioneModuloClienteInformazioniView(generics.RetrieveAPIView):

    queryset = Cliente.objects.all()
    lookup_field = 'id'  # Campo utilizzato per recuperare l'oggetto

    def retrieve(self, request, *args, **kwargs):
        
        cliente = self.get_object()
        cliente_serializer = ClientiSerializer(cliente)
        cliente_json = cliente_serializer.data

        ordine = Ordine.objects.filter(cliente=cliente).last()
        ordine_serializer = OrdineSerializer(ordine)
        ordine_json = ordine_serializer.data
        
        clienti_dati = DatiModuloInformazioniClienti.objects.filter(cliente=cliente).last()
        cliente_dati_serializer = InformazioniClientiSerializer(clienti_dati)
        cliente_dati_json = cliente_dati_serializer.data
        
        lista_patologie =[]
       
        for patologie in clienti_dati.patologie.all():
           
            lista_patologie.append(patologie.nome)
       

        data = {
            'cliente': cliente_json,
            'ordine': ordine_json,
            'cliente_data': cliente_dati_json,
            'lista_patologie': lista_patologie
           
        }
        print(data)
        return Response(data)

class CompilazioneModuloClienteAlimentiView(generics.RetrieveAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Cliente.objects.all()
    serializer_class = ClientiSerializer
    lookup_field = 'id'  # Campo utilizzato per recuperare l'oggetto

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        gusti_queryset = GustiClienti.objects.filter(cliente=instance)
        gusti_serializer = GustiClientiSerializer(gusti_queryset, many=True).data
        cliente_serializer = self.get_serializer(instance).data

        response_data = {
            'cliente': cliente_serializer,
            'gusti_alimenti': gusti_serializer
        }

        return Response(response_data)
    
   
   
