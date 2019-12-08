from django.db import models

# Create your models here.

class Postagem(models.Model):
    autor = models.ForeignKey("autor.Autor", on_delete=models.DO_NOTHING)
    #slug = models.SlugField(max_length=250)

    titulo = models.CharField(max_length=50)
    conteudo = models.TextField()
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_publicacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15,choices=(("Rascunho", ("Rascunho")),
                                                    ("Publicado", ("Publicado"))
                                                    ))

    def __str__(self):
        return self.titulo
