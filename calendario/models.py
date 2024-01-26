from email.policy import default
from django.db import models

# Create your models here.
class Appuntamento(models.Model):
    
    titolo = models.CharField(max_length=200)
    descrizione = models.TextField(blank=True, null=True)
    inizio = models.DateTimeField()
    fine = models.DateTimeField()
    effettuato = models.BooleanField( default = "False")

    def __str__(self):
        return self.titolo