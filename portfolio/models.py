from django.db import models


class Licenciatura(models.Model):
    nome = models.CharField(max_length=60)
    sigla = models.CharField(max_length=3, blank=True)
    instituicao = models.CharField(max_length=30, default="Universidade Lusófona")
    departamento = models.CharField(max_length=5, blank=True)
    ano_inicio = models.PositiveIntegerField()
    ano_fim_previsto = models.PositiveIntegerField()
    descricao = models.TextField(blank=True)
    site_oficial = models.URLField(blank=True)

    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=120)
    categoria = models.CharField(max_length=100, blank=True)  # achei melhor por isso pois um prof pode ser diretor de curso ou algo do tipo
    email_institucional = models.EmailField(blank=True)
    pagina_pessoal = models.URLField(blank=True)

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name="ucs") # on cascade pois se a licenciatura cair isso morre também
    nome = models.CharField(max_length=150)
    ano = models.PositiveSmallIntegerField()
    semestre = models.PositiveSmallIntegerField()
    ects = models.DecimalField(max_digits=4, decimal_places=1)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to="ucs/", blank=True, null=True)
    docentes = models.ManyToManyField(Docente, related_name="ucs")

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50,help_text="Ex: linguagem, framework, BD, ferramenta, etc.") # deve ter uma forma de fazer uma lista, talvez seja melhor
    descricao = models.TextField(blank=True)
    logo = models.ImageField(upload_to="tecnologias/", blank=True, null=True)
    site_oficial = models.URLField(blank=True)
    nivel_interesse = models.PositiveSmallIntegerField(help_text="Classificação 1-5, por exemplo.")
    destaques = models.TextField(blank=True,help_text="Aspetos mais relevantes (pontos fortes, casos de uso, etc.).")

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    uc = models.ForeignKey(
        UnidadeCurricular, on_delete=models.CASCADE, related_name="projetos"
    )
    titulo = models.CharField(max_length=150)
    resumo = models.TextField()
    conceitos_aplicados = models.TextField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name="projetos")
    imagem = models.ImageField(upload_to="projetos/", blank=True, null=True)
    video_demo = models.URLField(blank=True)
    repo_github = models.URLField(blank=True)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo


class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    ano_letivo = models.CharField(max_length=20)  # ex: 2024/2025
    autor = models.CharField(max_length=150)
    orientador = models.ForeignKey(
        Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name="tfcs"
    )
    resumo = models.TextField()
    area_tematica = models.CharField(max_length=150)
    classificacao = models.DecimalField(
        max_digits=4, decimal_places=1, blank=True, null=True
    )
    nivel_interesse = models.PositiveSmallIntegerField(
        help_text="Classificação pessoal de interesse (1-5)."
    )
    tecnologias = models.ManyToManyField(Tecnologia, related_name="tfcs", blank=True)
    repo_github = models.URLField(blank=True)
    documento = models.URLField(blank=True)

    def __str__(self):
        return self.titulo


class Competencia(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    nivel = models.CharField(
        max_length=50,
        help_text="Ex: Iniciante, Intermédio, Avançado."
    )
    categoria = models.CharField(
        max_length=80,
        help_text="Ex: Técnica, Soft Skill, Linguística, etc."
    )
    tecnologias_relacionadas = models.ManyToManyField(
        Tecnologia, related_name="competencias", blank=True
    )
    projetos_relacionados = models.ManyToManyField(
        Projeto, related_name="competencias", blank=True
    )
    tfcs_relacionados = models.ManyToManyField(
        TFC, related_name="competencias", blank=True
    )

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    titulo = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=150)
    tipo = models.CharField(
        max_length=80,
        help_text="Ex: Licenciatura, Curso curto, Certificação, Workshop."
    )
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    carga_horaria = models.PositiveIntegerField(blank=True, null=True)
    descricao = models.TextField(blank=True)
    certificado_url = models.URLField(blank=True)
    tecnologias = models.ManyToManyField(
        Tecnologia, related_name="formacoes", blank=True
    )

    class Meta:
        ordering = ["data_inicio", "data_fim"]

    def __str__(self):
        return self.titulo


class MakingOf(models.Model):
    ENTIDADE_CHOICES = [
        ("LICENCIATURA", "Licenciatura"),
        ("UC", "Unidade Curricular"),
        ("PROJETO", "Projeto"),
        ("TECNOLOGIA", "Tecnologia"),
        ("TFC", "TFC"),
        ("COMPETENCIA", "Competência"),
        ("FORMACAO", "Formação"),
    ]

    entidade_tipo = models.CharField(max_length=20, choices=ENTIDADE_CHOICES)
    entidade_id = models.PositiveIntegerField(
        help_text="ID da instância da entidade a que este registo se refere."
    )

    titulo = models.CharField(max_length=200)
    data_registo = models.DateTimeField(auto_now_add=True)
    descricao_processo = models.TextField(
        help_text="Descrição do processo de desenvolvimento/modelação."
    )
    decisoes_tomadas = models.TextField(blank=True)
    erros_encontrados = models.TextField(blank=True)
    correcoes = models.TextField(blank=True)
    justificacao_modelacao = models.TextField(blank=True)
    uso_ia = models.TextField(
        blank=True,
        help_text="Descrição de como ferramentas de IA foram usadas (ou não)."
    )

    evidencias_papel = models.ImageField(
        upload_to="makingof/", blank=True, null=True,
        help_text="Fotografias de caderno, DER, esquemas, etc."
    )

    relacionado_projeto = models.ForeignKey(
        Projeto, on_delete=models.SET_NULL, null=True, blank=True, related_name="making_of"
    )
    relacionado_uc = models.ForeignKey(
        UnidadeCurricular, on_delete=models.SET_NULL, null=True, blank=True, related_name="making_of"
    )
    relacionado_tfc = models.ForeignKey(
        TFC, on_delete=models.SET_NULL, null=True, blank=True, related_name="making_of"
    )
    relacionado_tecnologia = models.ForeignKey(
        Tecnologia, on_delete=models.SET_NULL, null=True, blank=True, related_name="making_of"
    )
    relacionado_formacao = models.ForeignKey(
        Formacao, on_delete=models.SET_NULL, null=True, blank=True, related_name="making_of"
    )

    def __str__(self):
        return f"{self.entidade_tipo} #{self.entidade_id} - {self.titulo}"
