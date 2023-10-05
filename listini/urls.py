from django.urls import path

from .apiview import GruppoListinoListView

app_name = 'listini'


urlpatterns = [

    path('lista/', GruppoListinoListView.as_view(), name='listini-list'),
    

]


