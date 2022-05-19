from asyncio.windows_events import NULL
from cmath import inf
import datetime
from django.shortcuts import redirect, render
from django.contrib import messages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from .models import *
from .forms import PSAForm, VariableForm
from bs4 import BeautifulSoup
from rpy2.robjects import r
import pandas as pd
from rpy2 import robjects as ro
from rpy2.robjects.conversion import localconverter
from rpy2.robjects import pandas2ri
from dateutil.relativedelta import relativedelta

# Create your views here.

pestania = "2"

def login(request):
    return render(request, "core/login.html")

def inicio(request):
    global pestania
    pestania = "2"
    columnas = ['ID', 'Fecha_Nacimiento', 'Fecha_Biopsia', 'Edad', 'Etnia', 'Obesidad', 'HTA', 'Diabetes', 'Tabaco', 'Familiar_CAP', 'TR_preop', 
                'Estadiaje_RM', 'Diam_max', 'ISUP_RM', 'Por_cores_pos', 'N_biopsias', 
                'Tipo_histologico', 'Gleason_biopsia', 'Gleason_pri', 'Gleason_sec', 'Num_cil_pos', 'Num_cil_neg', 'Por_cil_pos', 'Max_afeccion', 
                'Bilat', 'IPN', 'ILINF', 'IVASC', 'cTNM_biopsia', 'ISUP', 
                'Fecha_PRL', 'Tratamiento', 'Gleason_pieza_PRL', 'Gleason_pri_2', 'Gleason_sec_2', 'Bilat_2', 
                'Localiz_en_pieza', 'Multifocalidad', 'Volumen_tumoral', 'EEC', 'IVS', 
                'IPN_pieza', 'ILINF_pieza', 'IVASC_pieza', 'PINAG', 
                'MQP', 'TNM_pieza', 'T1_MTX',
                ]
    pacientes = Variables.objects.all().filter()
    seleccion = "Fecha_Biopsia,cTNM_biopsia,ISUP,Fecha_PRL,Gleason_pieza_PRL,Gleason_pri_2,Gleason_sec_2,EEC,IVS,MQP,TNM_pieza"
    if request.method == 'GET':
        if request.GET.get('ID'):
            if Variables.objects.all().filter(pk=request.GET.get('ID')):
                return redirect('http://127.0.0.1:8000/paciente/' + request.GET.get('ID') + '/')
            else:
                messages.error(request,'ID incorrecto')
        elif request.GET.get('crear'):
            return redirect('http://127.0.0.1:8000/paciente/')
        elif request.GET.get('filtro'):
            seleccion = request.GET.get('seleccion')
            atributo1 = NULL
            atributo2 = NULL
            if request.GET.get('asc1') == 'ASC':
                    orden1 = request.GET.get('orden1')
            else:
                orden1 = '-' + request.GET.get('orden1')
            if request.GET.get('asc2') == 'ASC':
                orden2 = request.GET.get('orden2')
            else:
                orden2 = '-' + request.GET.get('orden2')
            if request.GET.get('asc3') == 'ASC':
                orden3 = request.GET.get('orden3')
            else:
                orden3 = '-' + request.GET.get('orden3')
            
            if request.GET.get('operador1') and request.GET.get('operador1')=='=':
                atributo1 = request.GET.get('atributo1')
            elif request.GET.get('operador1') and request.GET.get('operador1')=='<':
                atributo1 = request.GET.get('atributo1') + '__lt'
            elif request.GET.get('operador1') and request.GET.get('operador1')=='>':
                atributo1 = request.GET.get('atributo1') + '__gt'
            elif request.GET.get('operador1') and request.GET.get('operador1')=='>=':
                atributo1 = request.GET.get('atributo1') + '__gte'
            elif request.GET.get('operador1') and request.GET.get('operador1')=='<=':
                atributo1 = request.GET.get('atributo1') + '__lte'
            if request.GET.get('operador2') and request.GET.get('operador2')=='=':
                atributo2 = request.GET.get('atributo2')
            elif request.GET.get('operador2') and request.GET.get('operador2')=='<':
                atributo2 = request.GET.get('atributo2') + '__lt'
            elif request.GET.get('operador2') and request.GET.get('operador2')=='>':
                atributo2 = request.GET.get('atributo2') + '__gt'
            elif request.GET.get('operador2') and request.GET.get('operador2')=='>=':
                atributo2 = request.GET.get('atributo2') + '__gte'
            elif request.GET.get('operador2') and request.GET.get('operador2')=='<=':
                atributo2 = request.GET.get('atributo2') + '__lte'

            if request.GET.get('texto1') and request.GET.get('texto2'):
                pacientes = Variables.objects.filter(**{atributo1: request.GET.get('texto1')}).filter(**{atributo2: request.GET.get('texto2')}).order_by(orden1, orden2, orden3)
            elif request.GET.get('texto1'):
                pacientes = Variables.objects.filter(**{atributo1: request.GET.get('texto1')}).order_by(orden1, orden2, orden3)
            elif request.GET.get('texto2'):
                pacientes = Variables.objects.filter(**{atributo2: request.GET.get('texto2')}).order_by(orden1, orden2, orden3)
            else:
                pacientes = Variables.objects.order_by(orden1, orden2, orden3)
    return render(request, "core/inicio.html", {'columnas' : columnas, 'pacientes' : pacientes, 'seleccion': seleccion})

def crearPaciente(request):
    if request.method == 'POST':
        form = VariableForm(request.POST)
        if form.is_valid():
            res = form.save()
            return redirect('http://127.0.0.1:8000/paciente/' + str(res.ID) + '/')
    else:
        form = VariableForm()
    return render(request, "core/formularios.html", {'form' : form, 'pestania': "2"})

def calcularDTM(id):
    psaPac = Psa.objects.all().filter(idPac = id)
    dtm = [0]
    if(psaPac):
        if len(psaPac) > 1:
            psaArray = []
            for muestra in psaPac:
                psaArray.append({'psa': muestra.psa, 'fecha': muestra.fecha})

            psaDataFrame = pd.DataFrame.from_dict(psaArray)
            
            with localconverter(ro.default_converter + pandas2ri.converter):
                rDataFrame = ro.conversion.py2rpy(psaDataFrame)

            r.assign('psaPac', rDataFrame)
            r('psa.lm <- lm(log2(psa) ~ fecha, psaPac)')
            r('dt <- 1/coef(psa.lm)[2]')
            r('dtm <- 12/365 * dt')
            dtm = r('dtm')
    return dtm

def calcularAnios(fecha1, fecha2):
    return relativedelta(fecha2, fecha1).years

def calcularTSEG(id, fecha):
    paciente = Variables.objects.all().filter(pk=id)
    return fecha - paciente[0].Fecha_Biopsia

def calcularPreRadical(id, psa, fecha):
    paciente = Variables.objects.all().filter(pk=id)
    
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://www.mskcc.org/nomograms/prostate/pre_op")

    hormoneTherapyFalse = browser.find_element_by_id("edit-neoadjuvant-hormone-therapy-false")
    browser.execute_script("arguments[0].click();", hormoneTherapyFalse)

    radiationTherapyFalse = browser.find_element_by_id("edit-neoadjuvant-radiation-therapy-false")
    browser.execute_script("arguments[0].click();", radiationTherapyFalse)

    age = browser.find_element_by_id("edit-age")
    age.send_keys(calcularAnios(paciente[0].Fecha_Nacimiento, fecha))

    prePSA = browser.find_element_by_id("edit-pre-treatment-psa")
    prePSA.send_keys(psa)

    browser.execute_script("document.getElementById('edit-primary-biopsy-gleason').getElementsByTagName('option')[0].setAttribute('value', '"
     + str(paciente[0].Gleason_pri) + "')")
    browser.execute_script("document.getElementById('edit-secondary-biopsy-gleason').getElementsByTagName('option')[0].setAttribute('value', '"
     + str(paciente[0].Gleason_sec) + "')")

    ctnmArray = ['', 'T1a', 'T2a', 'T2b', 'T2c', 'T3a', 'T3b', 'T4']
    browser.execute_script("document.getElementById('edit-clinical-tumor-stage-2010').getElementsByTagName('option')[0].setAttribute('value', '"
     + ctnmArray[paciente[0].cTNM_biopsia] + "')")

    NCilPos = browser.find_element_by_id("edit-biopsy-cores-positive")
    NCilPos.send_keys(paciente[0].Num_cil_pos)

    NCilNeg = browser.find_element_by_id("edit-biopsy-cores-negative")
    NCilNeg.send_keys(paciente[0].Num_cil_neg)

    calculateButton = browser.find_element_by_id("edit-submit")
    browser.execute_script("arguments[0].click();", calculateButton)

    body = browser.execute_script("return document.body")
    source = body.get_attribute('innerHTML') 
    soup = BeautifulSoup(source, "html.parser")
    values = soup.find_all("span", {"class": "value"})

    preRadical = {
        'prob_surv_10yr': int(values[0].string),
        'prob_surv_15yr': int(values[1].string),
        'prog_free_5yr': int(values[2].string),
        'prog_free_10yr': int(values[3].string),
        'prob_organ_confined': int(values[4].string),
        'prob_EEC': int(values[5].string),
        'prob_lymph_inolved': int(values[6].string),
        'prob_seminal_invasion': int(values[7].string)
    }

    return preRadical

def calcularPostRadical(id):
    paciente = Variables.objects.all().filter(pk=id)
    psaPac = Psa.objects.all().filter(idPac = id)
    fecha = datetime.date(2000,1,1)
    PSAs=0.01
    for psa in psaPac:
        if psa.fecha > fecha and psa.fecha <= paciente[0].Fecha_PRL:
            fecha = psa.fecha
            PSAs = psa.psa

    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://www.mskcc.org/nomograms/prostate/post_op")

    hormoneTherapyFalse = browser.find_element_by_id("edit-neoadjuvant-hormone-therapy-false")
    browser.execute_script("arguments[0].click();", hormoneTherapyFalse)

    radiationTherapyFalse = browser.find_element_by_id("edit-neoadjuvant-radiation-therapy-false")
    browser.execute_script("arguments[0].click();", radiationTherapyFalse)

    prePSA = browser.find_element_by_id("edit-pre-treatment-psa")
    prePSA.send_keys(PSAs)

    age = browser.find_element_by_id("edit-age-at-surgery")
    age.send_keys(calcularAnios(paciente[0].Fecha_Nacimiento, paciente[0].Fecha_PRL))

    risingPSA = browser.find_element_by_id("edit-months-disease-free")
    risingPSA.send_keys(calcularPSArising(id).days)

    browser.execute_script("document.getElementById('edit-primary-surgery-gleason').getElementsByTagName('option')[0].setAttribute('value', '"
     + str(paciente[0].Gleason_pri_2) + "')")
    browser.execute_script("document.getElementById('edit-secondary-surgery-gleason').getElementsByTagName('option')[0].setAttribute('value', '"
     + str(paciente[0].Gleason_sec_2) + "')")

    if paciente[0].MQP == 1 or paciente[0].MQP == 2:
        MQPos = browser.find_element_by_id("edit-surgical-margins-positive-true")
    else:
        MQPos = browser.find_element_by_id("edit-surgical-margins-positive-false")
    browser.execute_script("arguments[0].click();", MQPos)

    if paciente[0].EEC == 1:
        EECs = browser.find_element_by_id("edit-extracapsular-extension-true")
    else:
        EECs = browser.find_element_by_id("edit-extracapsular-extension-false")
    browser.execute_script("arguments[0].click();", EECs)

    if paciente[0].IVASC_pieza == 1:
        IVASCs = browser.find_element_by_id("edit-seminal-vesicle-involvement-true")
    else:
        IVASCs = browser.find_element_by_id("edit-seminal-vesicle-involvement-false")
    browser.execute_script("arguments[0].click();", IVASCs)

    if paciente[0].ILINF_pieza == 1:
        ILINFs = browser.find_element_by_id("edit-lymph-node-involvement-true")
    else:
        ILINFs = browser.find_element_by_id("edit-lymph-node-involvement-false")
    browser.execute_script("arguments[0].click();", ILINFs)

    calculateButton = browser.find_element_by_id("edit-submit")
    browser.execute_script("arguments[0].click();", calculateButton)

    body = browser.execute_script("return document.body")
    source = body.get_attribute('innerHTML') 
    soup = BeautifulSoup(source, "html.parser")
    values = soup.find_all("span", {"class": "value"})

    postRadical = {
        'POST_prob_surv_15yr': NULL,
        'POST_prog_free_5yr': int(values[0].string),
        'POST_prog_free_7yr': int(values[1].string),
        'POST_prog_free_10yr': int(values[2].string),
    }

    if len(values) > 3:
        print(postRadical)
        postRadical['POST_prob_surv_15yr'] = int(values[3].string)

    return postRadical

def calcularPSArising(id):
    psaPac = Psa.objects.all().filter(idPac = id).order_by('fecha')
    psaRising = 0
    fechaPsaRising = NULL
    fechaPRL = Variables.objects.all().filter(pk=id)[0].Fecha_PRL
    for psa1 in psaPac:
        if psa1.fecha > fechaPRL and psaRising < 0.2:
            psaRising = psa1.psa
            fechaPsaRising = psa1.fecha
    return (fechaPsaRising - fechaPRL)/30

def crearPaciente2(request, id):
    global pestania
    paciente = Variables.objects.all().filter(pk=id)
    psaPac = Psa.objects.all().filter(idPac = id).order_by('fecha')
    article = Variables.objects.get(pk=id)
    formPSA = PSAForm(request.POST)

    psas = []
    tduplis = []
    fechas = []
    psas.append(0)
    tduplis.append(0)
    for psa in psaPac:
        psas.append(psa.psa)
        tduplis.append(psa.tdupli)
        fechas.append(psa.fecha.strftime("%m/%d/%Y"))
    psas.append(0)
    tduplis.append(0)
    psas_s  = {
        "psas" : psas,
        "tduplis" : tduplis,
        "fechas" : fechas
    }

    if request.method == 'POST':
        form = VariableForm(request.POST, instance=article)
        pestania = request.POST.get('pestania')
        if form.is_valid() and request.POST.get('confirmar'):
            form.save()
        if request.POST.get('eliminarPSA') and request.POST.get('fecha'):
            Psa.objects.filter(fecha=request.POST.get('fecha')).delete()
        if formPSA.is_valid() and request.POST.get('confirmarPSA'):
            articlePsa = Psa.objects.all().filter(fecha = formPSA.data['fecha'])
            if len(articlePsa) > 0:
                formPSA = PSAForm(request.POST, instance=articlePsa[0])
            idPSA = formPSA.save()
            dtm = calcularDTM(id)
            tseg = calcularTSEG(id, idPSA.fecha)
            if not paciente[0].Fecha_PRL or (paciente[0].Fecha_PRL and paciente[0].Fecha_PRL > idPSA.fecha):
                if idPSA.psa >= 0.1 and paciente[0].Fecha_Nacimiento and paciente[0].Gleason_pri and paciente[0].Gleason_sec and paciente[0].cTNM_biopsia and paciente[0].Num_cil_pos and paciente[0].Num_cil_neg:
                    preRadical = calcularPreRadical(id, idPSA.psa, idPSA.fecha)
                    idPSA.prob_surv_10yr = preRadical['prob_surv_10yr']
                    idPSA.prob_surv_15yr = preRadical['prob_surv_15yr']
                    idPSA.prog_free_5yr = preRadical['prog_free_5yr']
                    idPSA.prog_free_10yr = preRadical['prog_free_10yr']
                    idPSA.prob_organ_confined = preRadical['prob_organ_confined']
                    idPSA.prob_EEC = preRadical['prob_EEC']
                    idPSA.prob_lymph_inolved = preRadical['prob_lymph_inolved']
                    idPSA.prob_seminal_invasion = preRadical['prob_seminal_invasion']
                else:
                    if idPSA.psa < 0.1:
                        messages.error(request, 'PSA menor que 0.1')
                    if not paciente[0].Fecha_Nacimiento:
                        messages.error(request, 'El paciente no tiene fecha de nacimiento')
                    if not paciente[0].Gleason_pri:
                        messages.error(request, 'El paciente no tiene gleason primario')
                    if not paciente[0].Gleason_sec:
                        messages.error(request, 'El paciente no tiene gleason secundario')
                    if not paciente[0].cTNM_biopsia:
                        messages.error(request, 'El paciente no tiene cTNM biopsia')
                    if not paciente[0].Num_cil_pos:
                        messages.error(request, 'El paciente no tiene número de cilindros positivos')
                    if not paciente[0].Num_cil_neg:
                        messages.error(request, 'El paciente no tiene número de cilindros negativos')
            else:
                if idPSA.psa >= 0.01 and paciente[0].Fecha_Nacimiento and paciente[0].Gleason_pri_2 and paciente[0].Gleason_sec_2 and paciente[0].MQP and paciente[0].EEC and paciente[0].IVASC_pieza and paciente[0].ILINF_pieza and paciente[0].Fecha_PRL:
                    postRadical = calcularPostRadical(id)
                    idPSA.POST_prob_surv_15yr = postRadical['POST_prob_surv_15yr']
                    idPSA.POST_prog_free_5yr = postRadical['POST_prog_free_5yr']
                    idPSA.POST_prog_free_7yr = postRadical['POST_prog_free_7yr']
                    idPSA.POST_prog_free_10yr = postRadical['POST_prog_free_10yr']
                else:
                    if idPSA.psa < 0.01:
                        messages.error(request, 'PSA menor que 0.1')
                    if not paciente[0].Fecha_Nacimiento:
                        messages.error(request, 'El paciente no tiene fecha de nacimiento')
                    if not paciente[0].Gleason_pri_2:
                        messages.error(request, 'El paciente no tiene gleason primario PRL')
                    if not paciente[0].Gleason_sec_2:
                        messages.error(request, 'El paciente no tiene gleason secundario PRL')
                    if not paciente[0].MQP:
                        messages.error(request, 'El paciente no tiene definido el valor de MQP')
                    if not paciente[0].EEC:
                        messages.error(request, 'El paciente no tiene definido el valor de EEC')
                    if not paciente[0].IVASC_pieza:
                        messages.error(request, 'El paciente no tiene definido el valor de IVASC pieza')
                    if not paciente[0].ILINF_pieza:
                        messages.error(request, 'El paciente no tiene definido el valor de ILINF pieza')
                    if not paciente[0].Fecha_PRL:
                        messages.error(request, 'El paciente no tiene fecha de PRL')

            if dtm[0] == inf or dtm[0] < 0:
                dtm[0] = 0
            if dtm:
                idPSA.tdupli = round(dtm[0], 2)
                idPSA.TSEG = round(tseg.days/30, 0)
                idPSA.save()
        return redirect('http://127.0.0.1:8000/paciente/' + str(id) + '/', {'pestania': pestania})
    else:
        form = VariableForm()
    return render(request, "core/formularios.html", {'form' : form, 'paciente': paciente[0], 'formPSA' : formPSA, 'idPac' : id, 'psaList': psaPac, 'pestania': pestania, 'psas': psas_s})
