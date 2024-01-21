from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


# Create your models here.

class RegimiFiscali(models.Model):

    nome_regime = models.CharField(max_length=20)
    descrizione = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_regime

    class Meta:
        verbose_name = "Regime Fiscale"
        verbose_name_plural = "Regimi Fiscali"

# Create your models here.


class AnagraficaUtente(models.Model):

    Livelli = (

        (0, '-------'),
        (1, 'Manager'),
        (2, 'Top Manager'),
        (3, 'Silver Manager'),
        (4, 'Gold Manager'),
        (5, 'Platinum Manager')

    )

    Titolare = (

        (1, 'Centro Benessere/Estetico'),
        (2, 'Palestra/Personal Trainer'),
        (3, 'Studio Specialista'),

    )

    CORNER_CHOICES = (

        (True, 'Corner'),
        (False, 'Centro Autorizzato')

    )

    PAGAMENTO_CHOICES = (

        (True, 'Unica Soluzione'),
        (False, 'Rateizzato')

    )

    # rapporto uno a uno con User
    utente = models.OneToOneField(
        User, null=True, blank=True, related_name='utente', on_delete=models.CASCADE)
    """ Dati Consulente """
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    luogo_di_nascita = models.CharField(max_length=50)
    provincia_di_nascita = models.CharField(max_length=2)
    data_nascita = models.DateField()
    codice_fiscale = models.CharField(max_length=16)
    indirizzo = models.CharField(max_length=100)
    numero_civico = models.CharField(max_length=5, null=True)
    cap = models.CharField(max_length=5)
    citta_di_residenza = models.CharField(max_length=25)
    provincia_di_residenza = models.CharField(max_length=2)
    regione_residenza = models.CharField(max_length=30)
    stato_residenza = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    cellulare = models.CharField(max_length=15)
    email = models.EmailField(max_length=150)
    banca_appoggio = models.CharField(max_length=100)
    iban = models.CharField(max_length=30)
    note = models.TextField(blank=True, null=True)
    corner = models.BooleanField(choices=CORNER_CHOICES, default=False)
    titolare_di = models.IntegerField(choices=Titolare, default=1)
    denominato = models.CharField(max_length=100)
    indirizzo_c = models.CharField(max_length=100)
    cap_c = models.CharField(max_length=10)
    comune = models.CharField(max_length=30)
    provincia = models.CharField(max_length=10)
    PICF = models.CharField(max_length=50)
    # numero_accordo = models.ForeignKey(to= 'amministrazione.AccordoNumeroCorner', on_delete=models.PROTECT,null=True, blank=True)
    formula_scelta = models.ForeignKey(
        to='FormulaCentro', on_delete=models.CASCADE, null=True, blank=True)
    pagamento = models.BooleanField(choices=PAGAMENTO_CHOICES, default=False)
    affiliatore = models.ForeignKey("self", on_delete=models.SET(
        "senza superiore"), null=True, blank=True, related_name='affiliati_anagrafica') 
    seguito = models.ForeignKey("self", on_delete=models.SET(
        "senza superiore"), null=True, blank=True, related_name='seguito_anagrafica')
   
    """ Struttura """
    # tipo_struttura = models.ForeignKey(Struttura,on_delete=models.SET_NULL,null=True,blank=True)
    superiore = models.ForeignKey("self", on_delete=models.SET(
        "senza superiore"), null=True, blank=True, related_name='superiore_anagrafica')
   
    """ Questionario informativo fisco """
    ruolo_altra_azienda = models.BooleanField(default=False)
    imponibile_provvigionale = models.FloatField(null=True, blank=True)
    imponibile_provvigionale_parole = models.CharField(
        max_length=11, default="", null=True, blank=True)
    partita_iva_ateco = models.BooleanField(default=False)
    partita_iva = models.CharField(
        max_length=11, default="", null=True, blank=True)
    gestione_separata_inps = models.BooleanField(default=False)
    regime = models.ForeignKey(RegimiFiscali, on_delete=models.CASCADE)

    """ date modifica """
    data_creazione = models.DateTimeField(auto_now_add=True)
    data_ultima_modifica = models.DateTimeField(auto_now_add=True)

    """Tipo Consulente"""
    # tipo_consulente = models.ForeignKey(RuoliConsulente,on_delete=models.SET_NULL,null=True,blank=True)
    livello_consulente = models.IntegerField(choices=Livelli, default=0)

    """ Informazioni Tesserino"""
    data_tesserino = models.DateField(null=True, blank=True)
    numero_tesserino = models.IntegerField(null=True, blank=True)
    numero_IVD = models.IntegerField(null=True, blank=True)

    """ informazione su dati myoffice"""
    id_seguito_intero = models.IntegerField(null=True, blank=True)
    id_affiliatore_intero = models.IntegerField(null=True, blank=True)
    id_superiore_intero = models.IntegerField(null=True, blank=True)
    id_myoffice_intero = models.IntegerField(null=True, blank=True)

    
    def __str__(self):
        return self.cognome + " " + self.nome

    class Meta:
        verbose_name = "Utente"
        verbose_name_plural = "Utenti"


class FormulaCentro(models.Model):

    nome = models.CharField(max_length=20)
    prezzo = models.CharField(max_length=10)
    premio = models.FloatField()

    def __str__(self):
        return str(self.nome)


# Create your models here.
