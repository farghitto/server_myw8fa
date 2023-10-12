from django.db import models


import datetime

# Create your models here.


def incremento_accordo():

    ultimo = AccordoNumero.objects.order_by('id').last()
    obj = datetime.now().year
    anno = str(obj)

    if not ultimo:  # aggiungere reset al nuovo anno

        return '0001' + '/' + anno

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

    ultimo = AccordoNumeroCorner.objects.order_by('id').last()
    obj = datetime.now().year
    anno = str(obj)

    if not ultimo:  # aggiungere reset al nuovo anno

        return '0051'

    numero_ordine = ultimo.numero_accordo
    numero_ordine_intero = int(numero_ordine)
    new_numero_ordine = numero_ordine_intero + 1
    new_numero_ordine_stringa = str(new_numero_ordine)

    return new_numero_ordine_stringa


class AccordoNumeroCorner(models.Model):

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
    numero_ordine = models.ForeignKey(AccordoNumero, on_delete=models.PROTECT)
    utente_inserimento = models.ForeignKey(to='utente.AnagraficaUtente', on_delete=models.PROTECT, related_name='ordini_come_utente_inserimento')
      

    """ Date """
    data_creazione = models.DateTimeField()
    data_ultima_modifica = models.DateTimeField(blank=True, null=True)
    
    """Programma"""
    programma = models.ForeignKey(to='listini.Programmi', on_delete=models.PROTECT, related_name='ordini_come_utente_inserimento')




    def __str__(self):
        return str(self.numero_ordine.numero_accordo) + "-" + str(self.cliente)

    class Meta:
        verbose_name = "Ordine"
        verbose_name_plural = "Ordini"



