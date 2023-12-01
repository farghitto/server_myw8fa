from rest_framework import serializers
from clienti.models import Cliente, StatoPeso
from clienti.models import GustiClienti
from clienti.models import PatologieClienti
from clienti.models import  Alimenti, DatiModuloInformazioniClienti


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


class AlimentiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimenti
        fields = '__all__'
        

class InformazioniClientiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatiModuloInformazioniClienti
        fields = '__all__'
        
        
        
class InformazioniClientiGustiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatiModuloInformazioniClienti
        fields = ['filosofia_alimentare', 'maiale']
        
        
class GustiClientiSerializer(serializers.ModelSerializer):
    class Meta:
        model = GustiClienti
        fields = '__all__'