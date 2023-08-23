from rest_framework import serializers
from .models import AnagraficaUtente
from rest_framework import generics




class UtenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnagraficaUtente
        fields = '__all__'
        


class UtenteListCreateView(generics.ListCreateAPIView):
    
    queryset = AnagraficaUtente.objects.all()
    serializer_class = UtenteSerializer