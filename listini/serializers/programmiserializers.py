from rest_framework import serializers
from listini.models import Programmi




class ProgrammiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmi
        fields = '__all__'