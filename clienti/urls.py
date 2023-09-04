from django.urls import path
from .apiview import ClienteListCreateView, ClienteRetrieveUpdateAPIView, InserisciMisuraClienteAPIView

app_name = 'clienti'



urlpatterns = [

    path('lista/', ClienteListCreateView.as_view(), name='cliente-list'),
    path('clienti/<int:id>/', ClienteRetrieveUpdateAPIView.as_view(), name='cliente_retrieve_update'),
    path('clientimisure/', InserisciMisuraClienteAPIView.as_view(), name='cliente_misure_create'),
    
]