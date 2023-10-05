from rest_framework import serializers
from listini.models import GruppoListino




class GruppoListinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GruppoListino
        fields = '__all__'
        
  
        