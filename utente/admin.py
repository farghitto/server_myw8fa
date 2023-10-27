from django.contrib import admin

from .models import AnagraficaUtente

# Register your models here.


class AnagraficaUtenteModelAdmin(admin.ModelAdmin):
    model = AnagraficaUtente
    
    list_display = ['utente','nome','cognome']
    search_fields = ['utente','nome','cognome']




admin.site.register(AnagraficaUtente, AnagraficaUtenteModelAdmin)
# Register your models here.
