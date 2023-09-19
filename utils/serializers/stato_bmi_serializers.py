from rest_framework import serializers
from models import StatoPeso




class statoPesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatoPeso
        fields = '__all__'
        
    
        


