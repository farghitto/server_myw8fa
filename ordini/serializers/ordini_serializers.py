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
    rate = RateSerializer(
        source='pagamento_set', many=True, read_only=True)

    class Meta:
        model = Pagamento
        fields = '__all__'


class OrdineinfoSerializer(serializers.ModelSerializer):
    cliente = ClientiSerializer()
    pagamenti = PagamentoSerializer(
        source='pagamento_set', many=True, read_only=True)

    class Meta:
        model = Ordine
        fields = '__all__'
