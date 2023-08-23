from django.urls import path
from .apiview import ClienteListCreateView

app_name = 'clienti'



urlpatterns = [

    path('lista/', ClienteListCreateView.as_view(), name='cliente-list'),
    
]