from django.urls import path

from .apiview import GruppoListinoListView, ProgrammiListView, GruppoBoolView

app_name = 'listini'


urlpatterns = [

    path('gruppi/', GruppoListinoListView.as_view(), name='listini-list'),
    path('sceltaprogrammi/', ProgrammiListView.as_view(),
         name='listini_programmi'),
    path('pagamenti/<int:pk>', GruppoBoolView.as_view(), name='listini-bool'),

]
