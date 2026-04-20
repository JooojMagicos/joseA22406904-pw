from django.urls import path
from . import views   # ✅ correto

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos/', views.cursos, name='cursos'),  
]