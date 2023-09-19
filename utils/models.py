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
