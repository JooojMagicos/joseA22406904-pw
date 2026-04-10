# populate_tfcs.py
# Correr com: python manage.py shell < populate_tfcs.py

import json
from portfolio.models import TFC, Tecnologia

with open('data/JEISO.json', encoding='utf-8') as f:
    dados = json.load(f)

criados = 0
ignorados = 0

for item in dados:
    # limpa espaços e pontos finais dos campos de texto
    def limpa(texto):
        return texto.strip().rstrip('.')

    titulo = limpa(item.get('titulo', ''))
    resumo = item.get('resumo', '') or ''
    orientador = ', '.join(limpa(o) for o in item.get('orientadores', []))
    ano_raw = item.get('ano', '2024')
    ano = int(str(ano_raw).strip())
    url_documento = item.get('pdf', '') or ''
    area_tematica = ', '.join(limpa(a) for a in item.get('areas', []))
    keywords = ', '.join(limpa(k) for k in item.get('palavras_chave', []))

    # evita duplicados pelo título
    if TFC.objects.filter(titulo=titulo).exists():
        ignorados += 1
        continue

    tfc = TFC.objects.create(
        titulo=titulo,
        resumo=resumo,
        orientador=orientador,
        ano=ano,
        url_documento=url_documento,
        area_tematica=area_tematica[:100],
        keywords=keywords,
    )

    # cria ou reutiliza tecnologias e associa ao TFC
    tecnologias_raw = item.get('tecnologias') or []
    for nome_raw in tecnologias_raw:
        nome = limpa(nome_raw)
        if not nome:
            continue
        tecnologia, _ = Tecnologia.objects.get_or_create(
            nome=nome,
            defaults={
                'categoria': 'Desconhecida',
                'descricao': '',
                'versao': '',
            }
        )
        tfc.tecnologias.add(tecnologia)

    criados += 1

print(f"Concluído: {criados} TFCs criados, {ignorados} ignorados (duplicados).")