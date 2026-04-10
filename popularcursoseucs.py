# populate_licenciatura_ucs.py
# Correr com: python manage.py shell < populate_licenciatura_ucs.py

import requests, json, os
from portfolio.models import Licenciatura, UnidadeCurricular, Docente

schoolYear = '202526'

courses = [
    457,   # meisi
    6347,  # mcid
    6614,  # mcid-sig
    260,   # lei
    1504,  # di
    12,    # lig
    2531,  # leirt
    6638,  # licma
    6634,  # lcid
]

for course in courses:
    for language in ['PT']:

        url = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'
        payload = {'language': language, 'courseCode': course, 'schoolYear': schoolYear}
        headers = {'content-type': 'application/json'}

        response = requests.post(url, json=payload, headers=headers)
        response_dict = response.json()

        licenciatura, _ = Licenciatura.objects.update_or_create(
            nome=response_dict.get('courseName', f'Curso {course}'),
            defaults={
                'grau':            response_dict.get('degreeType', ''),
                'ects_total':      int(response_dict.get('totalECTS') or 0),
                'duracao_anos':    int(response_dict.get('duration') or 3),
                'area_cientifica': response_dict.get('scientificArea', ''),
                'url_site':        response_dict.get('url', ''),
            }
        )

        for uc in response_dict['courseFlatPlan']:
            url = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails'
            payload = {'language': language, 'curricularIUnitReadableCode': uc['curricularIUnitReadableCode']}
            headers = {'content-type': 'application/json'}

            response_uc = requests.post(url, json=payload, headers=headers)
            response_uc_dict = response_uc.json()

            codigo = uc['curricularIUnitReadableCode']

            uc_obj, _ = UnidadeCurricular.objects.get_or_create(
                codigo=codigo,
                defaults={
                    'licenciatura':   licenciatura,
                    'nome':           response_uc_dict.get('curricularUnitName') or uc.get('name', codigo),
                    'ects':           int(response_uc_dict.get('ects') or uc.get('ects') or 0),
                    'ano_curricular': int(uc.get('curricularYear') or 1),
                    'semestre':       str(uc.get('semester') or 'S1'),
                    'descricao':      response_uc_dict.get('programContents') or '',
                }
            )

            # vincula ao curso atual independentemente de já existir noutro
            uc_obj.licenciatura = licenciatura if not UnidadeCurricular.objects.filter(codigo=codigo).exclude(licenciatura=licenciatura).exists() else uc_obj.licenciatura
            uc_obj.save()

            for doc in response_uc_dict.get('teachers') or []:
                nome_doc = doc.get('name', '')
                if not nome_doc:
                    continue
                docente_obj, _ = Docente.objects.get_or_create(
                    nome=nome_doc,
                    defaults={'email': doc.get('email', ''), 'titulo': doc.get('title', '')}
                )
                uc_obj.docentes.add(docente_obj)

            print(f"  {codigo} — {uc_obj.nome}")