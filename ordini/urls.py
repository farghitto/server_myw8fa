from django.urls import path

from .apiview import OrdiniListCreateView, OrdiniListView, OrdiniDetailView, NumeroOrdiniClienteView, OrdineUltimoView, DettagliOrdineView

app_name = 'ordini'


urlpatterns = [
    # Altri endpoint URL
    path('ordini/', OrdiniListCreateView.as_view(), name='ordini'),
    path('ordini/<int:cliente_id>', OrdiniListView.as_view(), name='ordini-cliente'),
    path('ordini/ultimo/<int:cliente_id>', OrdineUltimoView.as_view(), name='ordine_ultimo_cliente'),
    path('ordine/<int:id>', OrdiniDetailView.as_view(), name='ordine'),
    path('tipo_ordini/<int:id>', NumeroOrdiniClienteView.as_view(), name='ordine'),
    path('dettagli/<int:id>', DettagliOrdineView.as_view(), name='ordine_dettagli')
]