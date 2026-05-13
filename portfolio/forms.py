from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao, TipoTecnologia


class TipoTecnologiaForm(forms.ModelForm):
    class Meta:
        model = TipoTecnologia
        fields = ['nome', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }


class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ['tipo', 'nome', 'categoria', 'descricao', 'versao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'uc', 'ano', 'descricao', 'conceitos_uc', 'tecnologias']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'conceitos_uc': forms.Textarea(attrs={'rows': 3}),
            'tecnologias': forms.CheckboxSelectMultiple(),
        }


class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'tipo', 'descricao', 'tecnologias', 'projetos', 'formacoes']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'tecnologias': forms.CheckboxSelectMultiple(),
            'projetos': forms.CheckboxSelectMultiple(),
            'formacoes': forms.CheckboxSelectMultiple(),
        }


class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['nome', 'instituicao', 'tipo', 'data_inicio', 'data_fim', 'descricao', 'licenciatura']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }
