from rest_framework import serializers
from clienti.models import PersonalCheckUpCliente, Cliente


class MisureClientiSerializer(serializers.ModelSerializer):

    class Meta:

        model = PersonalCheckUpCliente
        fields = '__all__'


class CampiMisureSerializer(serializers.Serializer):
    class Meta:
        model = PersonalCheckUpCliente  # Sostituisci 'TuoModello' con il tuo modello reale
        exclude = ['cliente', 'data', 'id', 'peso_ottimale']
