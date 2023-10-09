from django.urls import path

from .apiview import GruppoListinoListView, ProgrammiListView

app_name = 'listini'


urlpatterns = [

    path('lista/<str:eta>', GruppoListinoListView.as_view(), name='listini-list'),
    path('sceltaprogrammi/', ProgrammiListView.as_view(),
         name='listini_programmi'),

]
