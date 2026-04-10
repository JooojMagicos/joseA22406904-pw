from portfolio.models import Licenciatura, UnidadeCurricular

UnidadeCurricular.objects.all().delete()
Licenciatura.objects.all().delete()