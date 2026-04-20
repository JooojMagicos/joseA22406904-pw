from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('tecnologias/', views.tecnologias_list, name='tecnologias'),
    path('projetos/', views.projetos_list, name='projetos'),
    path('tfcs/', views.tfcs_list, name='tfcs'),
    path('eventos/', views.eventos_list, name='eventos'),
    path('competencias/', views.competencias_list, name='competencias'),
    path('formacoes/', views.formacoes_list, name='formacoes'),
    path('ucs/', views.ucs_list, name='ucs'),
    path('licenciaturas/', views.licenciaturas_list, name='licenciaturas'),
    path('docentes/', views.docentes_list, name='docentes'),
]
