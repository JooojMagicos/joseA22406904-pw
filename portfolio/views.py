from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    Tecnologia, TipoTecnologia, Projeto, TFC, Evento,
    Competencia, Formacao, UnidadeCurricular,
    Licenciatura, Docente, MakingOf
)
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm, TipoTecnologiaForm


# ── Index ──────────────────────────────────────────────────────────────────

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


# ── Sobre ──────────────────────────────────────────────────────────────────

def sobre(request):
    tecnologias_por_tipo = {}
    for tipo in TipoTecnologia.objects.all():
        tecnologias_por_tipo[tipo] = tipo.tecnologias.all()
    sem_tipo = Tecnologia.objects.filter(tipo__isnull=True)
    making_of = MakingOf.objects.all().order_by('-data_registo')
    return render(request, 'portfolio/sobre.html', {
        'tecnologias_por_tipo': tecnologias_por_tipo,
        'sem_tipo': sem_tipo,
        'making_of': making_of,
    })


# ── Tecnologias ────────────────────────────────────────────────────────────

def tecnologias_list(request):
    return render(request, 'portfolio/tecnologias_list.html', {
        'tecnologias': Tecnologia.objects.select_related('tipo').order_by('nome'),
        'titulo': 'Tecnologias',
    })


def tecnologia_criar(request):
    form = TecnologiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/form_generic.html', {
        'form': form, 'titulo': 'Nova Tecnologia', 'cancelar_url': 'portfolio:tecnologias'
    })


def tecnologia_editar(request, pk):
    obj = get_object_or_404(Tecnologia, pk=pk)
    form = TecnologiaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/form_generic.html', {
        'form': form, 'titulo': f'Editar — {obj.nome}', 'cancelar_url': 'portfolio:tecnologias'
    })


def tecnologia_apagar(request, pk):
    obj = get_object_or_404(Tecnologia, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/confirmar_apagar.html', {
        'objeto': obj, 'titulo': f'Apagar Tecnologia: {obj.nome}', 'cancelar_url': 'portfolio:tecnologias'
    })


# ── TipoTecnologia ─────────────────────────────────────────────────────────

def tipotecnologias_list(request):
    return render(request, 'portfolio/tipotecnologias_list.html', {
        'tipos': TipoTecnologia.objects.all(),
        'titulo': 'Tipos de Tecnologia',
    })


def tipotecnologia_criar(request):
    form = TipoTecnologiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tipotecnologias')
    return render(request, 'portfolio/form_generic.html', {
        'form': form, 'titulo': 'Novo Tipo de Tecnologia', 'cancelar_url': 'portfolio:tipotecnologias'
    })


def tipotecnologia_editar(request, pk):
    obj = get_object_or_404(TipoTecnologia, pk=pk)
    form = TipoTecnologiaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tipotecnologias')
    return render(request, 'portfolio/form_generic.html', {
        'form': form, 'titulo': f'Editar — {obj}', 'cancelar_url': 'portfolio:tipotecnologias'
    })


def tipotecnologia_apagar(request, pk):
    obj = get_object_or_404(TipoTecnologia, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('portfolio:tipotecnologias')
    return render(request, 'portfolio/confirmar_apagar.html', {
        'objeto': obj, 'titulo': f'Apagar Tipo: {obj}', 'cancelar_url': 'portfolio:tipotecnologias'
    })


# ── Projetos ───────────────────────────────────────────────────────────────

def projetos_list(request):
    return render(request, 'portfolio/projetos_list.html', {
        'projetos': Projeto.objects.select_related('uc').prefetch_related('tecnologias').order_by('-ano'),
        'titulo': 'Projetos',
    })


def projeto_criar(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/form_generic.html', {
        'form': form, 'titulo': 'Novo Projeto', 'cancelar_url': 'portfolio:projetos'
    })


def projeto_editar(request, pk):
    obj = get_object_or_404(Projeto, pk=pk)
    form = ProjetoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/form_generic.html', {
        'form': form, 'titulo': f'Editar — {obj.titulo}', 'cancelar_url': 'portfolio:projetos'
    })


def projeto_apagar(request, pk):
    obj = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/confirmar_apagar.html', {
        'objeto': obj, 'titulo': f'Apagar Projeto: {obj.titulo}', 'cancelar_url': 'portfolio:projetos'
    })


# ── Competências ───────────────────────────────────────────────────────────

def competencias_list(request):
    return render(request, 'portfolio/competencias_list.html', {
        'competencias': Competencia.objects.prefetch_related('tecnologias').order_by('nome'),
        'titulo': 'Competências',
    })


def competencia_criar(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/form_generic.html', {
        'form': form, 'titulo': 'Nova Competência', 'cancelar_url': 'portfolio:competencias'
    })


def competencia_editar(request, pk):
    obj = get_object_or_404(Competencia, pk=pk)
    form = CompetenciaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/form_generic.html', {
        'form': form, 'titulo': f'Editar — {obj.nome}', 'cancelar_url': 'portfolio:competencias'
    })


def competencia_apagar(request, pk):
    obj = get_object_or_404(Competencia, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/confirmar_apagar.html', {
        'objeto': obj, 'titulo': f'Apagar Competência: {obj.nome}', 'cancelar_url': 'portfolio:competencias'
    })


# ── Formações ──────────────────────────────────────────────────────────────

def formacoes_list(request):
    return render(request, 'portfolio/formacoes_list.html', {
        'formacoes': Formacao.objects.all().order_by('-data_inicio'),
        'titulo': 'Formações',
    })


def formacao_criar(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/form_generic.html', {
        'form': form, 'titulo': 'Nova Formação', 'cancelar_url': 'portfolio:formacoes'
    })


def formacao_editar(request, pk):
    obj = get_object_or_404(Formacao, pk=pk)
    form = FormacaoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/form_generic.html', {
        'form': form, 'titulo': f'Editar — {obj.nome}', 'cancelar_url': 'portfolio:formacoes'
    })


def formacao_apagar(request, pk):
    obj = get_object_or_404(Formacao, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/confirmar_apagar.html', {
        'objeto': obj, 'titulo': f'Apagar Formação: {obj.nome}', 'cancelar_url': 'portfolio:formacoes'
    })


# ── Restantes (só leitura) ─────────────────────────────────────────────────

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
