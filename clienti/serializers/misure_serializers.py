from rest_framework import serializers
from clienti.models import PersonalCheckUpCliente



class MisureClientiSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = PersonalCheckUpCliente
        fields = '__all__'
        