# admin.py

from django.contrib import admin
from .models import (
    Licenciatura, UnidadeCurricular, Docente, Projeto,
    Tecnologia, TFC, Competencia, Formacao, MakingOf, Avaliacao
)


@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'grau', 'area_cientifica', 'duracao_anos', 'ects_total')
    search_fields = ('nome', 'area_cientifica')
    list_filter = ('grau',)


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'titulo', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('titulo',)


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'licenciatura', 'ano_curricular', 'semestre', 'ects')
    search_fields = ('nome', 'codigo', 'descricao')
    list_filter = ('licenciatura', 'ano_curricular', 'semestre')
    filter_horizontal = ('docentes',)


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'versao')
    search_fields = ('nome', 'descricao', 'categoria')
    list_filter = ('categoria',)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'uc', 'ano')
    search_fields = ('titulo', 'descricao', 'conceitos_uc')
    list_filter = ('ano', 'uc')
    filter_horizontal = ('tecnologias',)


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('uc', 'ano_letivo', 'semestre', 'nota_media', 'nr_alunos')
    search_fields = ('uc__nome',)
    list_filter = ('ano_letivo', 'semestre', 'uc')


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orientador', 'ano', 'area_tematica')
    search_fields = ('titulo', 'resumo', 'orientador', 'keywords', 'area_tematica')
    list_filter = ('ano', 'area_tematica')
    filter_horizontal = ('tecnologias',)


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')
    search_fields = ('nome', 'descricao')
    list_filter = ('tipo',)
    filter_horizontal = ('projetos', 'tecnologias', 'formacoes')


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'tipo', 'data_inicio', 'data_fim', 'licenciatura')
    search_fields = ('nome', 'instituicao', 'descricao')
    list_filter = ('tipo', 'instituicao', 'licenciatura')


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('entidade_relacionada', 'entidade_id', 'fase', 'data_registo')
    search_fields = ('descricao', 'decisoes', 'erros_correcoes', 'uso_ia')
    list_filter = ('entidade_relacionada', 'fase', 'data_registo')
