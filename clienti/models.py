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
    data_nascita = models.DateField()
    indirizzo = models.CharField(max_length=100)
    numero_civico = models.CharField(max_length=10, null=True)
    cap = models.CharField(max_length=5)
    citta = models.CharField(max_length=25)
    codice_fiscale = models.CharField(max_length=16)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    cellulare = models.CharField(max_length=15)
    altezza = models.CharField(max_length=7, blank=True, null=True)
    email = models.EmailField(max_length=150)
    sesso = models.CharField(max_length=1, choices=Sesso)
    note = models.TextField(blank=True, null=True)
    privacy = models.BooleanField(default=False)

    """ Consulente """
    consulente = models.ForeignKey(
        AnagraficaUtente, on_delete=models.SET_NULL, null=True)

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


# class PersonalCheckUpCliente(models.Model):

#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     data = models.DateField(auto_now_add=True)
#     peso = models.FloatField(verbose_name="Peso")
#     bmi = models.FloatField(verbose_name="Bmi")
#     grasso_corporeo = models.FloatField(
#         null=True, blank=True, verbose_name="Grasso corporeo")
#     muscolatura = models.FloatField(
#         null=True, blank=True, verbose_name="Muscolatura")
#     metabolismo = models.FloatField(
#         null=True, blank=True, verbose_name="Metabolismo")
#     grasso_viscerale = models.FloatField(
#         null=True, blank=True, verbose_name="Grasso viscerale")
#     collocm = models.FloatField(verbose_name="Centimetri collo")
#     toracecm = models.FloatField(verbose_name="Centimetri torace")
#     cosciadxcm = models.FloatField(verbose_name="Centimetri coscia destra")
#     cosciasxcm = models.FloatField(verbose_name="Centimetri coscia sinistra")
#     fianchicm = models.FloatField(verbose_name="Centimetri fianchi")
#     addomecm = models.FloatField(verbose_name="Centimetri addome")
#     ginocchiodxcm = models.FloatField(
#         verbose_name="Centimetri ginocchio destro")
#     ginocchiasxcm = models.FloatField(
#         verbose_name="Centimetri ginocchio sinistro")
#     peso_ottimale = models.CharField(max_length=6, null=True, blank=True)
#     peso_desiderato = models.CharField(max_length=6, null=True, blank=True)
#     programma = models.ForeignKey(
#         to='accordi.Programmi', on_delete=models.CASCADE, blank=True, null=True)

#     def __str__(self):

#         return self.cliente.cognome + ' ' + str(self.peso)


# class AnagraficaClienteDati(models.Model):

#     SCELTA = (

#         (1, 'Si'),
#         (0, 'No')
#     )

#     SCELTA3 = (

#         (0, 'No'),
#         (1, 'Si'),
#         (2, 'A volte')
#     )

#     CIVILE = (
#         ('Libero', 'Libero'),
#         ('Coniugato', 'Coniugato')
#     )

#     FISICO = (
#         ('A', 'A'),
#         ('B', 'B'),
#         ('C', 'C'),
#         ('D', 'D'),
#         ('E', 'E')
#     )

#     SCELTADIABETE = (

#         ('Tipo 1', 'Tipo 1'),
#         ('Tipo 2', 'Tipo 2')
#     )

#     MESIGRAVIDANZA = (
#         ('0', '0'),
#         ('1', '1'),
#         ('2', '2'),
#         ('3', '3'),
#         ('4', '4'),
#         ('5', '5'),
#         ('6', '6'),
#         ('7', '7'),
#         ('8', '8'),
#         ('9', '9')

#     )

#     GIORNI = (
#         ('0', '0'),
#         ('1', '1'),
#         ('2', '2'),
#         ('3', '3'),
#         ('4', '4'),
#         ('5', '5'),
#         ('6', '6'),
#         ('7', '7')
#     )

#     GRUPPO = (
#         ('N', 'Non so'),
#         ('0', '0'),
#         ('A', 'A'),
#         ('B', 'B'),
#         ('AB', 'AB')
#     )

#     ALIMENTAZIONE = (
#         ('Onnivoro', 'Onnivoro'),
#         ('Vegetariano', 'Vegetariano'),
#         ('Vegano', 'Vegano')
#     )
#     PRESSIONE = (
#         ('Normale', 'Normale'),
#         ('Ipoteso', 'Ipoteso'),
#         ('Iperteso', 'Iperteso')
#     )
#     ALIMENTI = (
#         ('Caffè', 'Caffè'),
#         ('Pane', 'Pane'),
#         ('Verdure', 'Verdure'),
#         ('Carne', 'Carne'),
#         ('Cereali', 'Cereali'),
#         ('Cioccolata', 'Cioccolata'),
#         ('Legumi', 'Legumi'),
#         ('Alcolici', 'Alcolici'),
#         ('Pasta', 'Pasta'),
#         ('Frutta', 'Frutta'),
#         ('Pesce', 'Pesce'),
#         ('Dolci', 'Dolci'),
#         ('Pizza', 'Pizza'),
#         ('Latticini', 'Latticini')
#     )

#     SAPORI = (
#         ('Piccante', 'Piccante'),
#         ('Dolce', 'Dolce'),
#         ('Salato', 'Salato'),
#         ('Amaro', 'Amaro'),
#         ('Aspro', 'Aspro'),
#         ('Insipido', 'Insipido')
#     )

#     CAR1 = (

#         (1, 'Individualista'),
#         (0, 'Altruista')
#     )

#     CAR2 = (

#         (1, 'Estroverso'),
#         (0, 'Introverso')
#     )

#     CAR3 = (

#         (1, 'Ottimista'),
#         (0, 'Pessimista')
#     )

#     SFOGO = (
#         ('Dentro', 'Dentro'),
#         ('Fuori', 'Fuori'),
#         ('Non so', 'Non so')
#     )

#     GIORNATA = (
#         ('Mattina', 'Mattina'),
#         ('Pomeriggio', 'Pomeriggio'),
#         ('Sera', 'Sera')
#     )

#     DETERMINATO = (
#         (0, '0'),
#         (1, '1'),
#         (2, '2'),
#         (3, '3'),
#         (4, '4'),
#         (5, '5'),
#         (6, '6'),
#         (7, '7'),
#         (8, '8'),
#         (9, '9'),
#         (10, '10')
#     )

#     PASTI = (
#         (1, 'Sempre'),
#         (2, 'Colazione'),
#         (3, 'Pranzo'),
#         (4, 'Cena'),
#         (5, 'Mai')

#     )

#     cliente = models.OneToOneField(
#         Cliente, related_name='cliente', on_delete=models.CASCADE)
#     provincia_nascita = models.CharField(max_length=50)
#     stato_nascita = models.CharField(max_length=50)
#     provincia = models.CharField(max_length=50)
#     stato = models.CharField(max_length=50)
#     professione = models.CharField(max_length=50)
#     stato_civile = models.CharField(
#         max_length=15, choices=CIVILE, default='Libero')
#     maggiorenne = models.BooleanField(choices=SCELTA, default=1)
#     peso_attuale = models.CharField(max_length=5)
#     altezza = models.CharField(max_length=5)
#     bmi = models.CharField(max_length=8)
#     stato_attuale = models.CharField(max_length=20)
#     peso_ottimale = models.CharField(max_length=5)
#     scostamento_peso = models.CharField(max_length=7)
#     peso_desiderato = models.CharField(max_length=5)
#     struttura_fisica = models.CharField(
#         max_length=1, choices=FISICO, default='A')
#     struttura_desiderata = models.CharField(
#         max_length=1, choices=FISICO, default='A')
#     pressione_arteriosa = models.CharField(
#         max_length=10, choices=PRESSIONE, default='Normale')
#     diabete = models.BooleanField(choices=SCELTA, default=0)
#     tipo_diabete = models.CharField(
#         max_length=10, choices=SCELTADIABETE, null=True, blank=True)
#     menopausa = models.BooleanField(choices=SCELTA, default=0)
#     gravidanza = models.BooleanField(choices=SCELTA, default=0)
#     mesi_gravidanza = models.CharField(
#         max_length=1, choices=MESIGRAVIDANZA, null=True, blank=True)
#     rapporto_corpo = models.IntegerField(choices=SCELTA3, default=0)
#     droghe = models.BooleanField(choices=SCELTA, default=0)
#     allergie = models.BooleanField(choices=SCELTA, default=0)
#     allergie_elenco = models.CharField(max_length=100, null=True, blank=True)
#     farmaci = models.BooleanField(choices=SCELTA, default=0)
#     farmaci_elenco = models.CharField(max_length=100, null=True, blank=True)
#     sport = models.BooleanField(choices=SCELTA, default=0)
#     sport_praticato = models.CharField(max_length=30, null=True, blank=True)
#     sport_praticato_giorni = models.CharField(
#         max_length=1, choices=GIORNI, null=True, blank=True)
#     gruppo_sanguigno = models.CharField(
#         max_length=7, choices=GRUPPO, default='N')
#     insonnia = models.IntegerField(choices=SCELTA3, default=0)
#     stitichezza = models.IntegerField(choices=SCELTA3, default=0)
#     fumo = models.BooleanField(choices=SCELTA, default=0)
#     numero_sigarette = models.CharField(max_length=3, null=True, blank=True)
#     delta_numero_sigarette = models.CharField(
#         max_length=3, null=True, blank=True)
#     fame_nervosa = models.IntegerField(choices=SCELTA3, default=0)
#     gengive = models.IntegerField(choices=SCELTA3, default=0)
#     tatuaggi = models.BooleanField(choices=SCELTA, default=0)
#     bevi_acqua = models.BooleanField(choices=SCELTA, default=0)
#     litri_acqua = models.CharField(max_length=5)
#     filosofia_alimentare = models.CharField(
#         max_length=15, choices=ALIMENTAZIONE, default=0)
#     maiale = models.BooleanField(choices=SCELTA, default=0)
#     figli = models.BooleanField(choices=SCELTA, default=0)
#     numero_figli = models.CharField(max_length=2, null=True, blank=True)
#     pasto_condiviso = models.IntegerField(choices=PASTI, null=True, blank=True)
#     # verifica, un intero non e valido come valore
#     alimenti_preferiti = MultiSelectField(
#         choices=ALIMENTI, max_length=20, default=0, null=True, blank=True)
#     gusti_preferiti = MultiSelectField(
#         choices=SAPORI,  max_length=20, default=0, null=True, blank=True)
#     patologie = models.ManyToManyField(PatologieClienti, null=True, blank=True)
#     problemi_cardiaci = models.BooleanField(choices=SCELTA, default=0)
#     problem_cardiaci_tipo = models.CharField(
#         max_length=100, null=True, blank=True)
#     sicura = models.IntegerField(choices=SCELTA3, default=0)
#     felice = models.IntegerField(choices=SCELTA3, default=0)
#     stress = models.IntegerField(choices=SCELTA3, default=0)
#     paure = models.IntegerField(choices=SCELTA3, default=0)
#     lutti = models.BooleanField(choices=SCELTA, default=0)
#     incubi = models.IntegerField(choices=SCELTA3, default=0)
#     stanco = models.CharField(max_length=14, choices=GIORNATA, default='Sera')
#     rabbia = models.IntegerField(choices=SCELTA3, default=0)
#     sfogo = models.CharField(max_length=9, choices=SFOGO, default='Non so')
#     colpa = models.BooleanField(choices=SCELTA, default=0)
#     piangi = models.BooleanField(choices=SCELTA, default=0)
#     carattere1 = models.BooleanField(choices=CAR1, default=0)
#     carattere2 = models.BooleanField(choices=CAR2, default=0)
#     carattere3 = models.BooleanField(choices=CAR3, default=0)
#     determinato = models.IntegerField(choices=DETERMINATO, default=0)
#     amici_dieta = models.BooleanField(choices=SCELTA, default=0)
#     note = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self):

#         return self.cliente.cognome


# # class DatiBiometrici(models.Model):

# #     dato_biometrico = models.CharField(max_length=50)

# #     def __str__(self):

# #         return self.dato_biometrico

# #     class Meta:
# #         verbose_name = "Dato Biometrico"
# #         verbose_name_plural = "Dati Biometrici"


# # class DatiBiometriciCliente(models.Model):

# #     cliente = models.ForeignKey(AnagraficaCliente, on_delete=models.CASCADE)
# #     data_creazione = models.DateTimeField(auto_now_add=True)
# #     valore = models.IntegerField()
# #     dato_biometrico = models.ForeignKey(
# #         DatiBiometrici, on_delete=models.CASCADE)

# #     def __str__(self):

# #         return self.cliente

# #     class Meta:
# #         verbose_name = "Dato Biometrico Cliente"
# #         verbose_name_plural = "Dati Biometrici Cliente"


# class IndirizziClienti(models.Model):

#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     indirizzo = models.CharField(max_length=100)
#     numero_civico = models.CharField(max_length=5, null=True)
#     cap = models.CharField(max_length=5)
#     citta = models.CharField(max_length=25)

#     class Meta:
#         verbose_name = "Indirizzo Cliente"
#         verbose_name_plural = "indirizzi Cliente"

#     def __str__(self):

#         return self.cliente.cognome + " " + self.indirizzo + " " + self.numero_civico + " " + self.citta


# class GustiClienti(models.Model):

#     ALIMENTICLIENTE = (
#         ('S', 'PRESENTE'),
#         ('A', 'ALLERGIA'),
#         ('I', 'INTOLLERANZA'),
#         ('N', 'NON GRADITO'),

#     )

#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     # alimento = models.ForeignKey(Alimenti, on_delete=models.CASCADE)
#     specifica = models.CharField(
#         max_length=1, choices=ALIMENTICLIENTE, default='S')


# class StatoPeso(models.Model):

#     sesso = models.CharField(max_length=1)
#     bmi = models.CharField(max_length=5)
#     qualitapeso = models.CharField(max_length=20)


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
