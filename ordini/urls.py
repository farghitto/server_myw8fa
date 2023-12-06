from django.urls import path

from .apiview import OrdiniListCreateView, OrdiniListView, OrdiniDetailView, NumeroOrdiniClienteView, OrdineUltimoView, DettagliOrdineView
from .apiview import CompilazioneModuloClienteOrdineView, ListaOrdiniView
from .apiview import CompilazioneModuloClienteInformazioniView
app_name = 'ordini'


urlpatterns = [
    # Altri endpoint URL
    path('ordini/', OrdiniListCreateView.as_view(), name='ordini'),
    path('ordini_lista/<int:consulente_id>',
         ListaOrdiniView.as_view(), name='ordini_lista'),
    path('ordini/<int:cliente_id>',
         OrdiniListView.as_view(), name='ordini-cliente'),
    path('ordini/ultimo/<int:cliente_id>',
         OrdineUltimoView.as_view(), name='ordine_ultimo_cliente'),
    path('ordine/<int:id>', OrdiniDetailView.as_view(), name='ordine'),
    path('tipo_ordini/<int:id>', NumeroOrdiniClienteView.as_view(), name='ordine'),
    path('dettagli/<int:id>', DettagliOrdineView.as_view(), name='ordine_dettagli'),
    
    path('datiordinepdf/<int:id>',
         CompilazioneModuloClienteOrdineView.as_view(), name='ordine_dettaglipdf'),
    
]
    

