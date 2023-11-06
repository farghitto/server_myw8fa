from django.db import models


from datetime import datetime

# Create your models here.


def incremento_accordo():

    ultimo = AccordoNumero.objects.order_by('id').last()
    obj = datetime.now().year
    anno = str(obj)

    if not ultimo:  # aggiungere reset al nuovo anno

        return '1' + '/' + anno

    numero_ordine = ultimo.numero_accordo
    numero_ordine_intero = int(numero_ordine.split('/')[0])
    new_numero_ordine = numero_ordine_intero + 1
    new_numero_ordine_stringa = str(new_numero_ordine) + '/' + anno

    return new_numero_ordine_stringa


class AccordoNumero(models.Model):

    numero_accordo = models.CharField(
        max_length=10, default=incremento_accordo)
    tipo_accordo = models.CharField(max_length=100)

    def __str__(self):
        return self.numero_accordo

    class Meta:
        verbose_name = "Numero Accordo"
        verbose_name_plural = "Numeri Accordi"


def incremento_accordo_corner():

    ultimo = AccordoNumeroAffilizaioneCentri.objects.order_by('id').last()
    obj = datetime.now().year
    anno = str(obj)

    if not ultimo:  # aggiungere reset al nuovo anno

        return '0051'

    numero_ordine = ultimo.numero_accordo
    numero_ordine_intero = int(numero_ordine)
    new_numero_ordine = numero_ordine_intero + 1
    new_numero_ordine_stringa = str(new_numero_ordine)

    return new_numero_ordine_stringa


class AccordoNumeroAffilizaioneCentri(models.Model):

    numero_accordo = models.CharField(
        max_length=10, default=incremento_accordo_corner)
    tipo_accordo = models.CharField(max_length=100)

    def __str__(self):
        return self.numero_accordo

    class Meta:
        verbose_name = "Numero Accordo Corner"
        verbose_name_plural = "Numeri Accordi Corner"



class Ordine(models.Model):

    cliente = models.ForeignKey(
        to='clienti.Cliente', on_delete=models.PROTECT)
    consulente = models.ForeignKey(
        to='utente.AnagraficaUtente', on_delete=models.PROTECT,  related_name='ordini_come_consulente')
    numero_ordine = models.ForeignKey(
        AccordoNumero, on_delete=models.PROTECT, blank=True, null=True)
    utente_inserimento = models.ForeignKey(
        to='utente.AnagraficaUtente', on_delete=models.PROTECT, related_name='ordini_come_utente_inserimento')
    ordine_confermato = models.BooleanField(default=False)

    """ Date """
    data_creazione = models.DateTimeField()
    data_ultima_modifica = models.DateTimeField(blank=True, null=True)
    data_ordine = models.DateTimeField(blank=True, null=True)
    """Programma"""
    programma = models.ForeignKey(
        to='listini.Programmi', on_delete=models.PROTECT, related_name='ordini_come_utente_inserimento')

    def __str__(self):
        return str(self.numero_ordine.numero_accordo) + "-" + str(self.cliente)

    class Meta:
        verbose_name = "Ordine"
        verbose_name_plural = "Ordini"


class Pagamento (models.Model):

    STATO = (
        ('Pagato', 'Pagamento Inserito'),
        ('Non Pagato', 'In Attesa del Pagamento')
    )
    TIPO = (
        ('Rateale', 'Rateale'),
        ('Unica Soluzione', 'Unica Soluzione')
    )

    ordine = models.OneToOneField(
        to='Ordine', on_delete=models.CASCADE)
    importo = models.DecimalField(max_digits=9, decimal_places=2)

    """ Dettagli Pagamenti"""
    tipo_pagamento = models.CharField(max_length=20, choices=TIPO)
    stato_ordine = models.CharField(max_length=20, choices=STATO)

    """ Date """
    data_pagamento = models.DateTimeField(blank=True, null=True)

    def effettua_pagamento(self):
        if self.stato_ordine == 'Non Pagato':
            if self.tipo_pagamento == 'Rateale':
                # Verifica se tutte le rate sono state pagate
                rate_non_pagate = self.rate_set.filter(
                    pagamento=self, pagato=False)
                if not rate_non_pagate:
                    # Segna lo stato dell'ordine come "Pagato" se tutte le rate sono state pagate
                    self.stato_ordine = 'Pagato'
                else:
                    # In caso contrario, le rate sono ancora in attesa di pagamento
                    self.stato_ordine = 'Non Pagato'
            else:
                # Se il pagamento non è rateale, segna direttamente lo stato dell'ordine come "Pagato"
                self.stato_ordine = 'Pagato'

            self.save()


class Rate (models.Model):

    pagamento = models.ForeignKey(to='Pagamento', on_delete=models.CASCADE)

    """Dettagli specifici di ciascuna rata"""
    numero_rata = models.IntegerField()
    importo_rata = models.DecimalField(max_digits=10, decimal_places=2)

    pagato = models.BooleanField(default=False)
    """ Date """
    data_pagamento = models.DateTimeField(blank=True, null=True)
    data_scadenza_rata = models.DateField()

    def effettua_pagamento_rata(self):
        if not self.pagato:
            # Esegui l'operazione di pagamento per la rata
            # Ad esempio, aggiorna lo stato del pagamento della rata
            self.pagato = True
            self.save()

            # Richiama il metodo per aggiornare lo stato del pagamento
            self.pagamento.effettua_pagamento()
