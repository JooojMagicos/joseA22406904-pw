from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),

    # Tecnologias
    path('tecnologias/', views.tecnologias_list, name='tecnologias'),
    path('tecnologias/nova/', views.tecnologia_criar, name='tecnologia_criar'),
    path('tecnologias/<int:pk>/editar/', views.tecnologia_editar, name='tecnologia_editar'),
    path('tecnologias/<int:pk>/apagar/', views.tecnologia_apagar, name='tecnologia_apagar'),

    # Tipos de Tecnologia
    path('tipotecnologias/', views.tipotecnologias_list, name='tipotecnologias'),
    path('tipotecnologias/novo/', views.tipotecnologia_criar, name='tipotecnologia_criar'),
    path('tipotecnologias/<int:pk>/editar/', views.tipotecnologia_editar, name='tipotecnologia_editar'),
    path('tipotecnologias/<int:pk>/apagar/', views.tipotecnologia_apagar, name='tipotecnologia_apagar'),

    # Projetos
    path('projetos/', views.projetos_list, name='projetos'),
    path('projetos/novo/', views.projeto_criar, name='projeto_criar'),
    path('projetos/<int:pk>/editar/', views.projeto_editar, name='projeto_editar'),
    path('projetos/<int:pk>/apagar/', views.projeto_apagar, name='projeto_apagar'),

    # Competências
    path('competencias/', views.competencias_list, name='competencias'),
    path('competencias/nova/', views.competencia_criar, name='competencia_criar'),
    path('competencias/<int:pk>/editar/', views.competencia_editar, name='competencia_editar'),
    path('competencias/<int:pk>/apagar/', views.competencia_apagar, name='competencia_apagar'),

    # Formações
    path('formacoes/', views.formacoes_list, name='formacoes'),
    path('formacoes/nova/', views.formacao_criar, name='formacao_criar'),
    path('formacoes/<int:pk>/editar/', views.formacao_editar, name='formacao_editar'),
    path('formacoes/<int:pk>/apagar/', views.formacao_apagar, name='formacao_apagar'),

    # Só leitura
    path('tfcs/', views.tfcs_list, name='tfcs'),
    path('eventos/', views.eventos_list, name='eventos'),
    path('ucs/', views.ucs_list, name='ucs'),
    path('licenciaturas/', views.licenciaturas_list, name='licenciaturas'),
    path('docentes/', views.docentes_list, name='docentes'),
]
