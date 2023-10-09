from django.db import models

# Create your models here.


class GruppoListino(models.Model):
    nome_gruppo = models.CharField(max_length=30, blank=False, null=False)
    descrizione_gruppo = models.CharField(
        max_length=250, blank=False, null=False)
    myw8fa_visibilita = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_gruppo

    class Meta:
        verbose_name = "Gruppo Listino"
        verbose_name_plural = "Gruppi Listino"


class Programmi(models.Model):
    """ Dati Programma """
    nome_programma = models.CharField(max_length=50, blank=False, null=False)
    descrizione_programma = models.CharField(
        max_length=250, blank=False, null=False)
    descrizione_in_fattura = models.CharField(
        max_length=250, blank=False, null=False)
    durata_programma = models.IntegerField(blank=True, null=True)
    importo = models.DecimalField(max_digits=7, decimal_places=2)
    fasce_kg = models.CharField(max_length=5, blank=True, null=True)

    codiceiva = models.ForeignKey(
        to='utils.CodiciIva', on_delete=models.CASCADE)
    listino_dedicato = models.ManyToManyField(
        'consulenti.Struttura', related_name="listino_dedicato", blank=True)

    """ Opzioni per le provvigioni"""
    validita_per_bilanciamento = models.BooleanField(default=False)
    programma_attivo = models.BooleanField(default=False)
    programma_intero = models.BooleanField(default=False)
    programma_amministratore = models.BooleanField(default=False)
    programma_kids = models.BooleanField(default=False)
    programma_rateale = models.BooleanField(default=False)
    programma_proseguimento = models.BooleanField(default=False)

    """informazioni inserimento"""
    data_creazione = models.DateField(auto_now_add=True)
    data_ultima_modifica = models.DateField(auto_now=True)

    """informazioni listino"""
    gruppo = models.ForeignKey(
        GruppoListino, on_delete=models.CASCADE, related_name='gruppo', null=True, blank=True)

    def __str__(self):
        return self.nome_programma + "-" + self.descrizione_programma

    class Meta:
        verbose_name = "Programma"
        verbose_name_plural = "Programma"
