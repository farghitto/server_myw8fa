from django.urls import path

from .apiview import GruppoListinoListView, ProgrammiListView

app_name = 'listini'


urlpatterns = [

    path('lista/', GruppoListinoListView.as_view(), name='listini-list'),
    path('sceltaprogrammi/<int:id>/', ProgrammiListView.as_view(),
         name='listini_programmi'),

]


