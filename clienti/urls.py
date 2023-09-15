from django.urls import path

from .apiview import InserisciMisuraClienteAPIView, MisuraClienteAPIView
from .apiview import ClienteListCreateView, ClienteRetrieveUpdateAPIView
from .apiview import CampiMisureAPI

app_name = 'clienti'


urlpatterns = [

    path('lista/', ClienteListCreateView.as_view(), name='cliente-list'),
    path('clienti/<int:id>/', ClienteRetrieveUpdateAPIView.as_view(),
         name='cliente_retrieve_update'),
    path('clientimisure/', InserisciMisuraClienteAPIView.as_view(),
         name='cliente_misure_create'),
    path('misure/<int:id>/', MisuraClienteAPIView.as_view(),
         name='cliente_retrieve_update'),
    path('api/campi_misure/', CampiMisureAPI.as_view(), name='campi-modello-api'),

]
