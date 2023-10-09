from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from django.shortcuts import get_object_or_404

from .serializers.gruppolistinoserializers import GruppoListinoSerializer
from .serializers.programmiserializers import ProgrammiSerializer

from .models import GruppoListino, Programmi
from consulenti.models import Struttura


class GruppoListinoListView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = GruppoListinoSerializer

    def get_queryset(self):

        eta = bool(self.kwargs['eta'])
        # modifica futura si dovrebbe vedere se il gruppo contiene programmi
        listino = get_object_or_404(Struttura, nome='Centro Autorizzato')
        programmi_validi = Programmi.objects.filter(
            programma_kids=eta, programma_attivo=True, listino_dedicato=listino)
        valori_unici = programmi_validi.values_list(
            'gruppo', flat=True).distinct()

        queryset = GruppoListino.objects.filter(id__in=valori_unici)
        return queryset


class ProgrammiListView(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProgrammiSerializer

    def get_queryset(self):

        listino = get_object_or_404(Struttura, nome='Centro Autorizzato')
        id = self.request.query_params.get('id')
        minore = self.request.query_params.get('minore')
        queryset = Programmi.objects.filter( programma_kids=minore, programma_attivo=True, listino_dedicato=listino, gruppo_id=id)
        return queryset
