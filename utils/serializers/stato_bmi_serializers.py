from rest_framework import serializers
from utils.models import StatoPeso, Bmiottimale


class statoPesoSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Bmiottimale
        fields = '__all__'
