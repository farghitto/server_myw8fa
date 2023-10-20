from rest_framework import serializers
from ordini.models import Ordine


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
