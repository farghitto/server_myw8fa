import pdb
from rest_framework import serializers
from ordini.models import Ordine, Pagamento, Rate
from clienti.serializers.cliente_serializers import ClientiSerializer


class OrdineRataSerializer(serializers.ModelSerializer):
    numero_rate = serializers.CharField(read_only=True)
    acconto = serializers.CharField(read_only=True)

    class Meta:
        model = Ordine
        fields = '__all__'


class OrdineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ordine
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'


class PagamentoSerializer(serializers.ModelSerializer):
    rate_set = RateSerializer(
         many=True, read_only=True)

    class Meta:
        model = Pagamento
        fields = '__all__'


class OrdineinfoSerializer(serializers.ModelSerializer):
    cliente = ClientiSerializer()
    pagamenti = PagamentoSerializer(source='pagamento', read_only=True)
    rate = serializers.SerializerMethodField()  # Campo personalizzato per le rate

    def get_rate(self, obj):
        try:
            if obj.pagamento.tipo_pagamento == 'Rateale':
                rate = obj.pagamento.rate_set.all()
                rate_serializer = RateSerializer(rate, many=True)
                return rate_serializer.data
        except AttributeError:
            pass  # Gestisci il caso in cui non ci sono rate


    class Meta:
        model = Ordine
        fields = '__all__'
