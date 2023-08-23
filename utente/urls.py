from django.urls import path

from .views import UtenteListCreateView


app_name = 'utente'

urlpatterns = [

    path('lista/', UtenteListCreateView.as_view(), name='cliente-list'),
   
    
]




