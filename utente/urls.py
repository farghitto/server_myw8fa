from django.urls import path

from .apiview import UtenteListCreateView, CreazioneUtenteView, CreazioneAnagraficaUtenteView


app_name = 'utente'

urlpatterns = [

    path('utente/<int:utente__id>',
         UtenteListCreateView.as_view(), name='cliente-list'),
    path('api/crea_utente/', CreazioneUtenteView.as_view(), name='crea_utente'),
    path('api/crea_anagrafica/', CreazioneAnagraficaUtenteView.as_view(), name='crea_anagrafica'),

]
