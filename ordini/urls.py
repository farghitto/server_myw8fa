from django.urls import path

from .apiview import OrdiniListCreateView, OrdiniListView, OrdiniDetailView, NumeroOrdiniClienteView

app_name = 'ordini'


urlpatterns = [
    # Altri endpoint URL
    path('ordini/', OrdiniListCreateView.as_view(), name='ordini'),
    path('ordini/<int:cliente_id>', OrdiniListView.as_view(), name='ordini-cliente'),
    path('ordine/<int:id>', OrdiniDetailView.as_view(), name='ordine'),
    path('tipo_ordini/<int:id>', NumeroOrdiniClienteView.as_view(), name='ordine'),
]