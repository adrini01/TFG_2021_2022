from django import forms
from .models import Psa, Variables

class VariableForm(forms.ModelForm):
    class Meta:
        model = Variables
        fields = [
            'Fecha_Biopsia',
            'Fecha_Nacimiento',
            'Edad',
            'Etnia',
            'Obesidad',
            'HTA',
            'Diabetes',
            'Tabaco',
            'Familiar_CAP',
            'TR_preop',
            # 'PSA_total',
            # 'psa_estratos',
            # 'PSAl_PSAt',
            # 'TDDUPRE',
            'Estadiaje_RM',
            'Diam_max',
            'ISUP_RM',
            'Por_cores_pos',
            'N_biopsias',
            'Tipo_histologico',
            'Gleason_biopsia',
            'Gleason_pri',
            'Gleason_sec',
            'Num_cil_pos',
            'Num_cil_neg',
            'Por_cil_pos',
            'Max_afeccion',
            'Bilat',
            'IPN',
            'ILINF',
            'IVASC',
            'cTNM_biopsia',
            'ISUP',
            'Fecha_PRL',
            'Tratamiento',
            'Gleason_pieza_PRL',
            'Gleason_pri_2',
            'Gleason_sec_2',
            'Bilat_2',
            'Localiz_en_pieza',
            'Multifocalidad',
            'Volumen_tumoral',
            'EEC',
            'IVS',
            'IPN_pieza',
            'ILINF_pieza',
            'IVASC_pieza' ,
            'PINAG' ,
            'MQP' ,
            'TNM_pieza' ,
            # 'PSA_pos',
            # 'tdupli' ,
            'T1_MTX' ,
            # 'Ultima_revision',
            # 'TSEG' ,
            # 'psafin',
        ]

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        # asi vuelves tus campos no requeridos
        self.fields['Fecha_Biopsia'].required = False
        self.fields['Fecha_Nacimiento'].required = False
        self.fields['Edad'].required = False
        self.fields['Etnia'].required = False
        self.fields['Obesidad'].required = False
        self.fields['HTA'].required = False
        self.fields['Diabetes'].required = False
        self.fields['Tabaco'].required = False
        self.fields['Familiar_CAP'].required = False
        self.fields['TR_preop'].required = False
        # self.fields['PSA_total'].required = False
        # self.fields['psa_estratos'].required = False
        # self.fields['PSAl_PSAt'].required = False
        # self.fields['TDDUPRE'].required = False
        self.fields['Estadiaje_RM'].required = False
        self.fields['Diam_max'].required = False
        self.fields['ISUP_RM'].required = False
        self.fields['Por_cores_pos'].required = False
        self.fields['N_biopsias'].required = False
        self.fields['Tipo_histologico'].required = False
        self.fields['Gleason_biopsia'].required = False
        self.fields['Gleason_pri'].required = False
        self.fields['Gleason_sec'].required = False
        self.fields['Num_cil_pos'].required = False
        self.fields['Num_cil_neg'].required = False
        self.fields['Por_cil_pos'].required = False
        self.fields['Max_afeccion'].required = False
        self.fields['Bilat'].required = False
        self.fields['IPN'].required = False
        self.fields['ILINF'].required = False
        self.fields['IVASC'].required = False
        self.fields['cTNM_biopsia'].required = False
        self.fields['ISUP'].required = False
        self.fields['Fecha_PRL'].required = False
        self.fields['Tratamiento'].required = False
        self.fields['Gleason_pieza_PRL'].required = False
        self.fields['Gleason_pri_2'].required = False
        self.fields['Gleason_sec_2'].required = False
        self.fields['Bilat_2'].required = False
        self.fields['Localiz_en_pieza'].required = False
        self.fields['Multifocalidad'].required = False
        self.fields['Volumen_tumoral'].required = False
        self.fields['EEC'].required = False
        self.fields['IVS'].required = False
        self.fields['IPN_pieza'].required = False
        self.fields['ILINF_pieza'].required = False
        self.fields['IVASC_pieza'].required = False
        self.fields['PINAG'].required = False
        self.fields['MQP'].required = False
        self.fields['TNM_pieza'].required = False
        # self.fields['PSA_pos'].required = False
        # self.fields['tdupli'].required = False
        self.fields['T1_MTX'].required = False
        # self.fields['Ultima_revision'].required = False
        # self.fields['TSEG'].required = False
        # self.fields['Ultimo_PSA'].required = False

class PSAForm(forms.ModelForm):
    class Meta:
        model = Psa
        fields = [ 'id', 'idPac', 'fecha', 'psa', 'tdupli', 'TSEG']
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['idPac'].required = False
        self.fields['idPac'].required = True
        self.fields['fecha'].required = True
        self.fields['psa'].required = True
        self.fields['tdupli'].required = False
        self.fields['TSEG'].required = False