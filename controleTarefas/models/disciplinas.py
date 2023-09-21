from django.db import models


class DisciplinasEntidade(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self) -> str:
        return "Disciplinas [%i - %s]" % (self.id, self.nome)


