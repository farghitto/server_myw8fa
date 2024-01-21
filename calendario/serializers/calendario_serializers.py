
from rest_framework import serializers
from calendario.models import Appuntamento





class AppuntamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appuntamento
        fields = '__all__'