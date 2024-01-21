from gc import get_objects
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from .models import AnagraficaUtente
from django.contrib.auth.models import User
from .serializers.utente_serializers import UtenteSerializer
from .serializers.user_serializers import UserSerializer
import pdb


class CustomAuthToken(APIView):

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id})
        else:
            return Response({'error': 'Credenziali non valide'}, status=401)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Invalida o elimina il token dell'utente
        request.auth.delete()  # Elimina il token di autenticazione personalizzato

        return Response(status.HTTP_200_OK)


class UtenteListCreateView(generics.RetrieveAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = AnagraficaUtente.objects.all()
    serializer_class = UtenteSerializer
    lookup_field = 'utente__id'


class CreazioneUtenteView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            return Response({"message": "Utente creato con successo"}, status=status.HTTP_201_CREATED)
        return response
    
    
class CreazioneAnagraficaUtenteView(generics.CreateAPIView):
    queryset = AnagraficaUtente.objects.all()
    serializer_class = UtenteSerializer
    

    def create(self, request, *args, **kwargs):
        # Fasi iniziali, inclusa la deserializzazione dei dati della richiesta
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        # Chiamata a perform_create
        self.perform_create(serializer)

        # Eventuale risposta HTTP di successo
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # Logica personalizzata o manipolazione dei dati prima del salvataggio
      
        utente =get_object_or_404(User, username= serializer.validated_data['email'] )
        serializer.validated_data['utente'] = utente
        serializer.save()