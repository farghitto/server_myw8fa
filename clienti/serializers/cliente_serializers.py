from rest_framework import serializers
from clienti.models import Cliente




class ClientiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def perform_create(self, serializer):
        instance = serializer.save()
        return instance    
        


