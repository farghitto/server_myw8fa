from django.urls import path

from .apiview import InserisciMisuraClienteAPIView, MisuraClienteAPIView, MisuraClientePesoInizialeAPIView
from .apiview import ClienteListCreateView, ClienteRetrieveUpdateAPIView, NuovoClienteAPIView, VerificaDatiCliente, ClienteCreateView, ClienteUpdateAPIView
from .apiview import CampiMisureAPI
from .apiview import StatoPesoAPIView
from .apiview import PatologieListAPIView, AlimentiListAPIView, InformazioniClientiCreateAPIView, InformazioniClientiGustiAPIView, ClientiGustiCreateAPIView
from .apiview import CompilazioneModuloClienteInformazioniView, CompilazioneModuloClienteAlimentiView

app_name = 'clienti'


urlpatterns = [

    path('lista/', ClienteListCreateView.as_view(), name='cliente-list'),
    path('clienti/<int:id>/', ClienteRetrieveUpdateAPIView.as_view(),
         name='cliente_retrieve_update'),
    path('nuovocliente/<int:id>/', NuovoClienteAPIView.as_view(),
         name='cliente_nuvo'),
    path('clientedati/<int:cliente_id>/', VerificaDatiCliente.as_view(),
         name='cliente_dati'),
    path('crea_cliente/', ClienteCreateView.as_view(),  name='crea_cliente' ),
    path('aggiornaclientemyoffice/<int:id_utente_myoffice>/', ClienteUpdateAPIView.as_view(),
         name='cliente_update'),
   
    path('listapatologie/', PatologieListAPIView.as_view(), name='pato-list'),
    path('listaalimenti/', AlimentiListAPIView.as_view(), name='alimenti-list'),
    
    path('inserisciinfo/', InformazioniClientiCreateAPIView.as_view(), name='info_create'),

    path('gusti/<int:cliente_id>/', InformazioniClientiGustiAPIView.as_view(), name='gusti'),
    path('inserimentogusti/', ClientiGustiCreateAPIView.as_view(), name='gusti'),

    path('clientimisure/', InserisciMisuraClienteAPIView.as_view(),
         name='cliente_misure_create'),
    path('misure/<int:id>/', MisuraClienteAPIView.as_view(),
         name='cliente_retrieve_update'),
    path('peso/<int:id>/', MisuraClientePesoInizialeAPIView.as_view(),
         name='cliente_retrieve_update'),
    path('api/campi_misure/', CampiMisureAPI.as_view(), name='campi-modello-api'),
    path('api/stati_peso/', StatoPesoAPIView.as_view(), name='stati_peso'),
    
    path('datimoduloinfopdf/<int:id>',
         CompilazioneModuloClienteInformazioniView.as_view(), name='clienti_info_dettaglipdf'),
    path('datimoduloalimentipdf/<int:id>',
         CompilazioneModuloClienteAlimentiView.as_view(), name='clienti_info_dettaglipdf')
    

]
