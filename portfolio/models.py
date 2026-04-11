from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    grau = models.CharField(max_length=50)
    ects_total = models.IntegerField()
    duracao_anos = models.IntegerField()
    area_cientifica = models.CharField(max_length=100)
    url_site = models.URLField()

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    docentes = models.ManyToManyField(Docente, related_name='ucs')
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20)
    ects = models.IntegerField()
    ano_curricular = models.IntegerField()
    semestre = models.CharField(max_length=10)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.codigo} — {self.nome}"

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    descricao = models.TextField()
    versao = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    conceitos_uc = models.TextField()
    ano = models.IntegerField()

    def __str__(self):
        return self.titulo

class Avaliacao(models.Model):
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name='avaliacoes')
    ano_letivo = models.IntegerField()
    semestre = models.CharField(max_length=10)
    nota_media = models.DecimalField(max_digits=4, decimal_places=2)
    nr_alunos = models.IntegerField()

    def __str__(self):
        return f"{self.uc} — {self.ano_letivo} {self.semestre}"

class TFC(models.Model):
    tecnologias = models.ManyToManyField(Tecnologia, related_name='tfcs')
    titulo = models.CharField(max_length=300)
    resumo = models.TextField()
    orientador = models.CharField(max_length=200)
    ano = models.IntegerField()
    url_documento = models.URLField(blank=True)
    area_tematica = models.CharField(max_length=100)
    keywords = models.CharField(max_length=300)

    def __str__(self):
        return self.titulo

class Competencia(models.Model):
    projetos = models.ManyToManyField(Projeto, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    formacoes = models.ManyToManyField('Formacao', blank=True)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Formacao(models.Model):
    licenciatura = models.ForeignKey(Licenciatura, null=True, blank=True, on_delete=models.SET_NULL)
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class MakingOf(models.Model):
    entidade_relacionada = models.CharField(max_length=50)
    entidade_id = models.IntegerField()
    descricao = models.TextField()
    decisoes = models.TextField()
    erros_correcoes = models.TextField(blank=True)
    foto_papel = models.ImageField(upload_to='makingof/', blank=True)
    data_registo = models.DateField(auto_now_add=True)
    uso_ia = models.TextField(blank=True)
    fase = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.entidade_relacionada} — {self.fase}"

class Evento(models.Model):
    TIPO_CHOICES = [
        ('hackathon', 'Hackathon'),
        ('conferencia', 'Conferência'),
        ('workshop', 'Workshop'),
        ('webinar', 'Webinar'),
        ('outro', 'Outro'),
    ]
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    local = models.CharField(max_length=200, blank=True)
    certificado = models.FileField(upload_to='eventos/certificados/', blank=True)
    imagem = models.ImageField(upload_to='eventos/', blank=True)
    tecnologias = models.ManyToManyField('Tecnologia', blank=True, related_name='eventos')

    def __str__(self):
        return self.nome