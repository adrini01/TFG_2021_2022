from django.db import models

# Create your models here.

class Medico(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    nick = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

class Variables(models.Model):
    ID = models.AutoField(primary_key = True)
    Fecha_Biopsia = models.DateField(null= True)
    Fecha_Nacimiento = models.DateField(null= True)
    Edad = models.IntegerField(null= True)
    Etnia = models.IntegerField(null= True)
    Obesidad = models.IntegerField(null= True)
    HTA = models.IntegerField(null= True)
    Diabetes = models.IntegerField(null= True)
    Tabaco = models.IntegerField(null= True)
    Familiar_CAP = models.IntegerField(null= True)
    TR_preop = models.IntegerField(null= True)
    # PSA_total = models.FloatField(null= True)
    # psa_estratos = models.IntegerField(null= True)
    # PSAl_PSAt = models.FloatField(null= True)
    # TDDUPRE = models.IntegerField(null= True)
    Estadiaje_RM = models.IntegerField(null= True)
    Diam_max = models.FloatField(null= True)
    ISUP_RM = models.IntegerField(null= True)
    Por_cores_pos = models.FloatField(null= True)
    N_biopsias = models.IntegerField(null= True)
    Tipo_histologico = models.IntegerField(null= True)
    Gleason_biopsia = models.IntegerField(null= True)
    Gleason_pri = models.IntegerField(null= True)
    Gleason_sec = models.IntegerField(null= True)
    Num_cil_pos = models.IntegerField(null= True)
    Num_cil_neg = models.IntegerField(null= True)
    Por_cil_pos = models.FloatField(null= True)
    Max_afeccion = models.FloatField(null= True)
    Bilat = models.IntegerField(null= True)
    IPN = models.IntegerField(null= True)
    ILINF = models.IntegerField(null= True)
    IVASC = models.IntegerField(null= True)
    cTNM_biopsia = models.IntegerField(null= True)
    ISUP = models.IntegerField(null= True)
    Fecha_PRL = models.DateField(null= True)
    Tratamiento = models.IntegerField(null= True)
    Gleason_pieza_PRL = models.IntegerField(null= True)
    Gleason_pri_2 = models.IntegerField(null= True)
    Gleason_sec_2 = models.IntegerField(null= True)
    Bilat_2 = models.IntegerField(null= True)
    Localiz_en_pieza = models.IntegerField(null= True)
    Multifocalidad = models.IntegerField(null= True)
    Volumen_tumoral = models.FloatField(null= True)
    EEC = models.IntegerField(null= True)
    IVS = models.IntegerField(null= True)
    IPN_pieza = models.IntegerField(null= True)
    ILINF_pieza = models.IntegerField(null= True)
    IVASC_pieza = models.IntegerField(null= True)
    PINAG = models.IntegerField(null= True)
    MQP = models.IntegerField(null= True)
    TNM_pieza = models.IntegerField(null= True)
    # PSA_pos = models.FloatField(null= True)
    # tdupli = models.IntegerField(null= True)
    T1_MTX = models.IntegerField(null= True)
    # Ultima_revision = models.DateField(null= True)
    # TSEG = models.IntegerField(null= True)
    # Ultimo_PSA = models.FloatField(null= True)

class Psa(models.Model):
    idPac =  models.ForeignKey('Variables', on_delete=models.CASCADE)
    psa =  models.FloatField()
    fecha = models.DateField()
    tdupli =  models.FloatField(null= True)
    TSEG = models.FloatField(null= True)
    prob_surv_10yr = models.IntegerField(null= True)
    prob_surv_15yr = models.IntegerField(null= True)
    prog_free_5yr = models.IntegerField(null= True)
    prog_free_10yr = models.IntegerField(null= True)
    prob_organ_confined = models.IntegerField(null= True)
    prob_EEC = models.IntegerField(null= True)
    prob_lymph_inolved = models.IntegerField(null= True)
    prob_seminal_invasion = models.IntegerField(null= True)
    POST_prog_free_5yr = models.IntegerField(null= True) 
    POST_prog_free_7yr = models.IntegerField(null= True)
    POST_prog_free_10yr = models.IntegerField(null= True)
    POST_prob_surv_15yr = models.IntegerField(null= True)