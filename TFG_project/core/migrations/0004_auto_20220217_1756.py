# Generated by Django 3.2.9 on 2022-02-17 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220214_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variables',
            old_name='bilat',
            new_name='Bilat',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='bilat2',
            new_name='Bilat_2',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='dm',
            new_name='Diabetes',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='cores_pos',
            new_name='Diam_max',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='edad',
            new_name='EEC',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='estadiaje_rm',
            new_name='Edad',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='etnia',
            new_name='Estadiaje_RM',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='extracap',
            new_name='Etnia',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='gleason1_pri',
            new_name='Familiar_CAP',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='fecha_prl',
            new_name='Fecha_Biopsia',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='fechacir',
            new_name='Fecha_PRL',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='gleason1_sec',
            new_name='Gleason_biopsia',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='gleason1a',
            new_name='Gleason_pieza_PRL',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='gleason2_pri',
            new_name='Gleason_pri',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='gleason2_sec',
            new_name='Gleason_pri_2',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='gleason2a',
            new_name='Gleason_sec',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='hereda',
            new_name='Gleason_sec_2',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='histo',
            new_name='ILINF_pieza',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='ilinf2',
            new_name='IPN',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='iperin',
            new_name='IPN_pieza',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='iperin2',
            new_name='ISUP_RM',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='isup_bio',
            new_name='IVASC',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='ivascu',
            new_name='IVASC_pieza',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='ivascu2',
            new_name='IVS',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='localiz',
            new_name='Localiz_en_pieza',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='margen',
            new_name='MQP',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='diametro_max',
            new_name='Max_afeccion',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='multifoc',
            new_name='Multifocalidad',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='nbiopsia',
            new_name='N_biopsias',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='obeso',
            new_name='Obesidad',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='pinag',
            new_name='PINAG',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='max_af_cil',
            new_name='Por_cores_pos',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='t1mtx',
            new_name='T1_MTX',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='tabaco',
            new_name='TDDUPRE',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='tactor',
            new_name='TNM_pieza',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='tduppre',
            new_name='TR_preop',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='tnm1',
            new_name='TSEG',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='tnm2',
            new_name='Tabaco',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='tratamiento',
            new_name='Tipo_histologico',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='tsegui',
            new_name='Tratamiento',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='fechafin',
            new_name='Ultima_revision',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='volumen',
            new_name='Volumen_tumoral',
        ),
        migrations.RenameField(
            model_name='variables',
            old_name='vvss',
            new_name='cTNM_biopsia',
        ),
    ]
