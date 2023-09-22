from django.db import models

class AlunosEntidade(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self) -> str:
        return "Alunos [%i - %s]" % (self.id, self.nome)


  