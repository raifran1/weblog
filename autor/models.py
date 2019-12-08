from django.db import models

# Create your models here.
class Autor(models.Model):
    nome_completo = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=30,choices=(("Masculino", ("Masculino")),
                                        ("Feminino", ("Feminino")),
                                        ("Outro", ("Outro"))),
                                        default="")
    email = models.CharField(max_length=60)
    ocupacao = models.CharField(max_length=50,choices=(("Estudante", ("Estudante")),
                                        ("Professor", ("Professor")),
                                        ("Pesquisador", ("Pesquisador")),
                                        ("Entusiasta", ("Entusiasta")),
                                        ("Outro", ("Outro"))),
                                        default="")
    #ocupacao_2 = models.CharField(max_length=80, blank=True, null=True)
    resumo_perfil = models.TextField()
    #foto_autor = models.FileField(upload_to=None, max_length=100)

    def __str__(self):
        return self.nome_completo