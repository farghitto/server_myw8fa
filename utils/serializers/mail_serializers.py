from rest_framework import serializers
from utils.models import EmailAzienda


class emailSerializer(serializers.ModelSerializer):
    class Meta:

        model = EmailAzienda
        fields = '__all__'
