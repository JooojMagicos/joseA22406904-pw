from django.shortcuts import render
from .models import (
    Tecnologia, Projeto, TFC, Evento,
    Competencia, Formacao, UnidadeCurricular,
    Licenciatura, Docente
)


def index(request):
    context = {
        'stats': [
            ('Tecnologias', Tecnologia.objects.count()),
            ('Projetos', Projeto.objects.count()),
            ('TFCs', TFC.objects.count()),
            ('Eventos', Evento.objects.count()),
            ('Competências', Competencia.objects.count()),
            ('Formações', Formacao.objects.count()),
            ('Unidades Curriculares', UnidadeCurricular.objects.count()),
            ('Licenciaturas', Licenciatura.objects.count()),
            ('Docentes', Docente.objects.count()),
        ]
    }
    return render(request, 'portfolio/index.html', context)


def tecnologias_list(request):
    return render(request, 'portfolio/tecnologias_list.html', {
        'tecnologias': Tecnologia.objects.all().order_by('nome'),
        'titulo': 'Tecnologias',
    })


def projetos_list(request):
    return render(request, 'portfolio/projetos_list.html', {
        'projetos': Projeto.objects.all().order_by('-ano'),
        'titulo': 'Projetos',
    })


def tfcs_list(request):
    return render(request, 'portfolio/tfcs_list.html', {
        'tfcs': TFC.objects.all().order_by('-ano'),
        'titulo': 'Trabalhos de Fim de Curso',
    })


def eventos_list(request):
    return render(request, 'portfolio/eventos_list.html', {
        'eventos': Evento.objects.all().order_by('-data_inicio'),
        'titulo': 'Eventos',
    })


def competencias_list(request):
    return render(request, 'portfolio/competencias_list.html', {
        'competencias': Competencia.objects.all().order_by('nome'),
        'titulo': 'Competências',
    })


def formacoes_list(request):
    return render(request, 'portfolio/formacoes_list.html', {
        'formacoes': Formacao.objects.all().order_by('-data_inicio'),
        'titulo': 'Formações',
    })


def ucs_list(request):
    return render(request, 'portfolio/ucs_list.html', {
        'ucs': UnidadeCurricular.objects.all().order_by('ano_curricular', 'nome'),
        'titulo': 'Unidades Curriculares',
    })


def licenciaturas_list(request):
    return render(request, 'portfolio/licenciaturas_list.html', {
        'licenciaturas': Licenciatura.objects.all().order_by('nome'),
        'titulo': 'Licenciaturas',
    })


def docentes_list(request):
    return render(request, 'portfolio/docentes_list.html', {
        'docentes': Docente.objects.all().order_by('nome'),
        'titulo': 'Docentes',
    })
