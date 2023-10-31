from django.urls import path

from .apiview import InserisciMisuraClienteAPIView, MisuraClienteAPIView, MisuraClientePesoInizialeAPIView
from .apiview import ClienteListCreateView, ClienteRetrieveUpdateAPIView, NuovoClienteAPIView, VerificaDatiCliente
from .apiview import CampiMisureAPI

app_name = 'clienti'


urlpatterns = [

    path('lista/', ClienteListCreateView.as_view(), name='cliente-list'),
    path('clienti/<int:id>/', ClienteRetrieveUpdateAPIView.as_view(),
         name='cliente_retrieve_update'),
    path('nuovocliente/<int:id>/', NuovoClienteAPIView.as_view(),
         name='cliente_nuvo'),
    path('clientedati/<int:cliente_id>/', VerificaDatiCliente.as_view(),
         name='cliente_dati'),
    
    
    path('clientimisure/', InserisciMisuraClienteAPIView.as_view(),
         name='cliente_misure_create'),
    path('misure/<int:id>/', MisuraClienteAPIView.as_view(),
         name='cliente_retrieve_update'),
    path('peso/<int:id>/', MisuraClientePesoInizialeAPIView.as_view(),
         name='cliente_retrieve_update'),
    path('api/campi_misure/', CampiMisureAPI.as_view(), name='campi-modello-api'),

]
