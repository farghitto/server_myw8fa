from rest_framework import serializers
from utente.models import AnagraficaUtente




class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnagraficaUtente
        fields = '__all__'