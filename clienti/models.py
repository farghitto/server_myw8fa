from django.db import models
from utente.models import AnagraficaUtente
# from amministrazione.models import Alimenti
from multiselectfield import MultiSelectField

# Create your models here.


class Cliente(models.Model):

    Sesso = (

        ('M', 'M'),
        ('F', 'F')
    )

    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    citta_nascita = models.CharField(max_length=25)
    provincia_nascita = models.CharField(max_length=25)
    stato_nascita = models.CharField(max_length=25)
    data_nascita = models.DateField()
    indirizzo = models.CharField(max_length=100)
    numero_civico = models.CharField(max_length=10, null=True)
    cap = models.CharField(max_length=5)
    citta = models.CharField(max_length=25)
    provincia_residenza = models.CharField(max_length=25)
    stato_residenza = models.CharField(max_length=25)
    codice_fiscale = models.CharField(max_length=16)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    cellulare = models.CharField(max_length=15)
    altezza = models.CharField(max_length=7, blank=True, null=True)
    email = models.EmailField(max_length=150)
    sesso = models.CharField(max_length=1, choices=Sesso)
    note = models.TextField(blank=True, null=True)

    peso_desiderato = models.CharField(max_length=6, null=True, blank=True)

    """ Consulente """
    consulente = models.ForeignKey(
        to='utente.AnagraficaUtente', on_delete=models.SET_NULL, null=True)

    """ Date modifica """
    data_creazione = models.DateTimeField(auto_now_add=True)
    data_ultima_modifica = models.DateTimeField(auto_now_add=True)

    """ Dati Anagrafici Persona Giuridica"""
    ragione_sociale = models.CharField(max_length=100, null=True, blank=True)
    sede = models.CharField(max_length=50, blank=True, null=True, default="")
    indirizzo_sede = models.CharField(
        max_length=100, null=True, blank=True, default="")
    cap_sede = models.CharField(
        max_length=5, null=True, blank=True, default="")
    telefono_sede = models.CharField(
        max_length=15, null=True, blank=True, default="")
    email_sede = models.EmailField(
        max_length=100, null=True, blank=True, default="")
    partita_iva = models.CharField(max_length=11, null=True, blank=True)
    codice_univoco = models.CharField(max_length=8, null=True, blank=True)

    """Dati Anagrafici Beneficiario"""
    beneficiario_nome = models.CharField(max_length=50, null=True, blank=True)
    beneficiario_cognome = models.CharField(
        max_length=50, null=True, blank=True)
    beneficiario_cellulare = models.CharField(
        max_length=15, null=True, blank=True)
    beneficiario_codice_fiscale = models.CharField(
        max_length=16, null=True, blank=True)

    """Compilazione allegati"""

    compilazione_pcu = models.BooleanField(default=False)
    privacy = models.BooleanField(default=False)
    """Utente da collegare nell'app"""

    id_utente_app = models.CharField(max_length=8, null=True, blank=True)
    lingua_utente = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):

        return self.nome + " " + self.cognome

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clienti"


class PatologieClienti(models.Model):

    COLPITI = (
        ('T', 'Tutti'),
        ('U', 'Uomo'),
        ('D', 'Donna')
    )

    nome = models.CharField(max_length=50)
    patologia_sesso = models.CharField(
        max_length=1, choices=COLPITI, default=0)

    def __str__(self):

        return self.nome


class PersonalCheckUpCliente(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    peso = models.FloatField(verbose_name="Peso")
    bmi = models.FloatField(verbose_name="Bmi")
    grasso_corporeo = models.FloatField(
        null=True, blank=True, verbose_name="Grasso corporeo")
    muscolatura = models.FloatField(
        null=True, blank=True, verbose_name="Muscolatura")
    metabolismo = models.FloatField(
        null=True, blank=True, verbose_name="Metabolismo")
    grasso_viscerale = models.FloatField(
        null=True, blank=True, verbose_name="Grasso viscerale")
    collocm = models.FloatField(verbose_name="Centimetri collo")
    toracecm = models.FloatField(verbose_name="Centimetri torace")
    cosciadxcm = models.FloatField(verbose_name="Centimetri coscia destra")
    cosciasxcm = models.FloatField(verbose_name="Centimetri coscia sinistra")
    fianchicm = models.FloatField(verbose_name="Centimetri fianchi")
    addomecm = models.FloatField(verbose_name="Centimetri addome")
    ginocchiodxcm = models.FloatField(
        verbose_name="Centimetri ginocchio destro")
    ginocchiosxcm = models.FloatField(
        verbose_name="Centimetri ginocchio sinistro")
    peso_ottimale = models.CharField(max_length=6, null=True, blank=True)

#     programma = models.ForeignKey(
#         to='accordi.Programmi', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):

        return self.cliente.cognome + ' ' + str(self.peso)


class DatiModuloInformazioniClienti(models.Model):

    cliente = models.OneToOneField(
        Cliente, related_name='cliente', on_delete=models.CASCADE)
    professione = models.CharField(max_length=50)
    stato_civile = models.CharField(max_length=15)
    maggiorenne = models.CharField(max_length=5)
    peso_attuale = models.CharField(max_length=5)
    altezza = models.CharField(max_length=5)
    bmi = models.CharField(max_length=8)
    stato_attuale = models.CharField(max_length=20)
    peso_ottimale = models.CharField(max_length=5)
    scostamento_peso = models.CharField(max_length=7)
    peso_desiderato = models.CharField(max_length=5)
    struttura_fisica = models.CharField(max_length=1)
    struttura_desiderata = models.CharField(max_length=1)
    pressione_arteriosa = models.CharField(max_length=10)
    diabete = models.CharField(max_length=5)
    tipo_diabete = models.CharField(max_length=10, null=True, blank=True)
    menopausa = models.CharField(max_length=5, null=True, blank=True)
    gravidanza = models.CharField(max_length=5, null=True, blank=True)
    mesi_gravidanza = models.CharField(max_length=5, null=True, blank=True)
    rapporto_corpo = models.CharField(max_length=10)
    droghe = models.CharField(max_length=5)
    allergie = models.CharField(max_length=5)
    allergie_elenco = models.CharField(max_length=1000, null=True, blank=True)
    farmaci = models.CharField(max_length=5)
    farmaci_elenco = models.CharField(max_length=1000, null=True, blank=True)
    sport = models.CharField(max_length=5)
    sport_praticato = models.CharField(max_length=300, null=True, blank=True)
    sport_praticato_giorni = models.CharField(
        max_length=5, null=True, blank=True)
    gruppo_sanguigno = models.CharField(max_length=7)
    insonnia = models.CharField(max_length=5)
    stitichezza = models.CharField(max_length=5)
    fumo = models.CharField(max_length=5)
    numero_sigarette = models.CharField(max_length=3, null=True, blank=True)
    delta_numero_sigarette = models.CharField(
        max_length=3, null=True, blank=True)
    fame_nervosa = models.CharField(max_length=5)
    gengive = models.CharField(max_length=5)
    tatuaggi = models.CharField(max_length=5)
    bevi_acqua = models.CharField(max_length=5)
    litri_acqua = models.CharField(max_length=5)
    filosofia_alimentare = models.CharField(max_length=20)
    maiale = models.CharField(max_length=5)
    figli = models.CharField(max_length=5)
    numero_figli = models.CharField(max_length=2, null=True, blank=True)
    pasto_condiviso = models.CharField(max_length=10, null=True, blank=True)
    # verifica, un intero non e valido come valore
    alimenti_preferiti = models.TextField(blank=True, null=True)
    gusti_preferiti = models.TextField(blank=True, null=True)
    patologie = models.ManyToManyField(PatologieClienti, blank=True)
    problemi_cardiaci =  models.CharField(max_length=5)
    problem_cardiaci_tipo = models.CharField(
        max_length=100, null=True, blank=True)
    sicura = models.CharField(max_length=9)
    felice = models.CharField(max_length=9)
    stress = models.CharField(max_length=9)
    paure = models.CharField(max_length=9)
    lutti = models.CharField(max_length=9)
    incubi = models.CharField(max_length=9)
    stanco = models.CharField(max_length=14)
    rabbia = models.CharField(max_length=9)
    sfogo = models.CharField(max_length=9)
    colpa = models.CharField(max_length=9)
    piangi = models.CharField(max_length=9)
    carattere1 = models.CharField(max_length=20)
    carattere2 = models.CharField(max_length=20)
    carattere3 = models.CharField(max_length=20)
    determinato = models.CharField(max_length=9)
    amici_dieta = models.CharField(max_length=9)
    note = models.CharField(max_length=100, null=True, blank=True)
    firmato = models.BooleanField(default=0)

    def __str__(self):

        return self.cliente.cognome


class Alimenti(models.Model):

    CLASSE = (
        ('Legumi', 'Legumi'),
        ('Latticini', 'Latticini'),
        ('Frutta secca', 'Frutta secca'),
        ('Uovo', 'Uovo'),
        ('Tacchino', 'Tacchino'),
        ('Manzo', 'Manzo'),
        ('Maiale', 'Maiale'),
        ('Coniglio', 'Coniglio'),
        ('Vitello', 'Vitello'),
        ('Agnello', 'Agnello'),
        ('Frutta', 'Frutta'),
        ('Verdura', 'Verdura'),
        ('Pesce', 'Pesce'),
        ('Pollo', 'Pollo'),
        ('Crostacei', 'Crostacei'),
        ('Molluschi', 'Molluschi'),
    )

    nome = models.CharField(max_length=50)
    classe_alimenti = models.CharField(max_length=25, choices=CLASSE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Alimento"
        verbose_name_plural = "Alimenti"


class GustiClienti(models.Model):


    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimenti, on_delete=models.CASCADE)
    allergia = models.BooleanField(default=0)
    data_inserimento = models.DateTimeField(auto_now_add=True)


class StatoPeso(models.Model):

    sesso = models.CharField(max_length=1)
    bmi = models.CharField(max_length=5)
    qualitapeso = models.CharField(max_length=20)


# class Bmiottimale(models.Model):

#     sesso = models.CharField(max_length=20, blank=False, null=False)
#     valore = models.DecimalField(max_digits=7, decimal_places=2)
#     costituzione = models.CharField(max_length=20, blank=True, null=True)
#     eta = models.IntegerField(blank=True, null=True)
#     morfologia = models.CharField(max_length=20, blank=True, null=True)

#     def __str__(self):
#         return self.sesso + ' ' + str(self.valore)

#     class Meta:
#         verbose_name = "Bmi ottimale"
#         verbose_name_plural = "Bmi ottimale"


# # class Messaggi_interni (models.Model):

# #     TIPOMESSAGIO = (
# #         ('M', 'Mediche'),
# #         ('G', 'Generiche'),
# #         ('A', 'Amministrative'),


# #     )

# #     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
# #     utente_mittente = models.ForeignKey(
# #         Anagrafica, related_name='mittente', on_delete=models.CASCADE)
# #     utente_destinazione = models.ForeignKey(
# #         AnagraficaConsulente, related_name='destinatario', on_delete=models.CASCADE)
# #     data_inserimento = models.DateField(auto_now_add=True)
# #     letto = models.BooleanField(default=False)
# #     testo = models.TextField(max_length=500)
# #     tipo = models.CharField(max_length=1, choices=TIPOMESSAGIO, default='G')
# #     conversazione = models.IntegerField(max_length=10000)

# #     def __str__(self):
# #         return self.cliente.cognome + ' messaggio: ' + self.testo

# #     class Meta:
# #         verbose_name = "Informazioni Medico-Cliente"
# #         verbose_name_plural = "Informazioni Medico-Cliente"


# # Create your models here.
