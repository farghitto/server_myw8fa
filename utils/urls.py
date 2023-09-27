from django.urls import path

from .apiview import StatoBmi, EmailAziendaRetrive


app_name = 'utils'


urlpatterns = [

    path('statobmi/<int:id>/<str:bmi>', StatoBmi.as_view(), name='stato_bmi'),
    path('email/<int:id>', EmailAziendaRetrive.as_view(), name='email'),

]
