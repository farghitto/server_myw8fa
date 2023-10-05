from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from django.shortcuts import get_object_or_404

from .serializers.gruppolistinoserializers import GruppoListinoSerializer
from .serializers.programmiserializers import ProgrammiSerializer

from .models import GruppoListino, Programmi


class GruppoListinoListView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = GruppoListinoSerializer

    def get_queryset(self):

        queryset = GruppoListino.objects.filter(myw8fa_visibilita=True)
        return queryset


class ProgrammiListView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProgrammiSerializer

    def get_queryset(self):
        
        id = self.kwargs['id']
        queryset = Programmi.objects.filter(gruppo_id=id)
        return queryset