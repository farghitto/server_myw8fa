from rest_framework import serializers
from ordini.models import Ordine




class OrdineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordine
        fields = '__all__'
        
   