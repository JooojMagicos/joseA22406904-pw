from django.shortcuts import render
from .models import Curso   # 👈 importante



def index(request):
    return render(request, 'escola/index.html')



def cursos(request):
    cursos = Curso.objects.all()  

    return render(request, 'escola/cursos.html', {
        'cursos': cursos
    })