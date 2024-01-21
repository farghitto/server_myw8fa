from django.urls import path

from .apiview import AppuntamentoListCreateView, AppuntamentoRetrieveUpdateAPIView, AppuntamentoDestroyAPIView


app_name = 'calendario'


urlpatterns = [

    path('crea_appuntamento/', AppuntamentoListCreateView.as_view(), name='crea_appuntamento'),
    path('appuntamento/<int:id>/', AppuntamentoRetrieveUpdateAPIView.as_view(),
         name='appuntamento_retrieve_update'),
    path('elimina_appuntamento/<int:id>/', AppuntamentoDestroyAPIView.as_view(),
         name='appuntamento_delete'),
]