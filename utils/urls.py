from django.urls import path

from .apiview import StatoBmi


app_name = 'utils'


urlpatterns = [

    path('statobmi/<int:id>/<str:bmi>', StatoBmi.as_view(), name='stato_bmi'),


]
