from django.urls import path

from .apiview import UtenteListCreateView


app_name = 'utente'

urlpatterns = [

    path('utente/<int:utente__id>',
         UtenteListCreateView.as_view(), name='cliente-list'),


]
