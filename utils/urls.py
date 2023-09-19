from django.urls import path

from .apiview import 


app_name = 'utils'


urlpatterns = [

    path('statobmi/<int:id>', StatoBmi.as_view(), name='cliente-list'),
    

]