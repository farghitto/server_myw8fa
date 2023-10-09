from django.contrib import admin
from .models import Programmi, GruppoListino

# Register your models here.


class ProgrammaModelAdmin(admin.ModelAdmin):
    model = Programmi

    list_display = ["nome_programma", "descrizione_programma", "data_ultima_modifica", "gruppo",
                    "validita_per_bilanciamento", "programma_attivo", "programma_intero", "programma_proseguimento",
                    "programma_rateale","programma_kids"]
    search_fields = ["nome_programma", "descrizione_programma"]


class GruppoListinoModelAdmin(admin.ModelAdmin):
    model = GruppoListino

    list_display = ["nome_gruppo", "descrizione_gruppo"]
    search_fields = ["nome_gruppo"]


admin.site.register(Programmi, ProgrammaModelAdmin)
admin.site.register(GruppoListino, GruppoListinoModelAdmin)


# Register your models here.
