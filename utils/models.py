from django.db import models


class Bmiottimale(models.Model):

    sesso = models.CharField(max_length=20, blank=False, null=False)
    valore = models.DecimalField(max_digits=7, decimal_places=2)
    costituzione = models.CharField(max_length=20, blank=True, null=True)
    eta = models.IntegerField(blank=True, null=True)
    morfologia = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.sesso + ' ' + str(self.valore)

    class Meta:
        verbose_name = "Bmi ottimale"
        verbose_name_plural = "Bmi ottimale"


class StatoPeso(models.Model):

    sesso = models.CharField(max_length=1)
    bmi = models.CharField(max_length=5)
    qualitapeso = models.CharField(max_length=20)


class EmailAzienda(models.Model):

    descrizione = models.CharField(max_length=50)
    email = models.EmailField(max_length=150, blank=True, null=True)
    testo_oggetto = models.CharField(max_length=50)
    testo_mail = models.TextField(blank=True, null=True)
    bcc = models.EmailField(max_length=150, blank=True, null=True)
    bcc2 = models.EmailField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.descrizione

    class Meta:
        verbose_name = "Email Azienda"
        verbose_name_plural = "Email Azienda"


class CodiciIva(models.Model):

    nome = models.CharField(max_length=3)
    valore = models.IntegerField()
    descrizione = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Codice Iva"
        verbose_name_plural = "Codici Iva"
