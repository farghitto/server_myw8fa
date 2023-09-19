from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers.stato_bmi_serializers import statoPesoSerializer

class StatoBmi(generics.GenericAPIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = statoPesoSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valore_inserito = serializer.validated_data['valore_inserito']
        risultato = valore_inserito * 2
        return Response({'risultato': risultato})