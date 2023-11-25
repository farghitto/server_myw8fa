from rest_framework import serializers
from clienti.models import Cliente, StatoPeso, PatologieClienti


class ClientiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def perform_create(self, serializer):
        instance = serializer.save()
        return instance


class StatoPesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatoPeso
        fields = '__all__'


class PatologieSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatologieClienti
        fields = '__all__'
