from django.db import models
from ..models.disciplinas import DisciplinasEntidade
from ..models.alunos import AlunosEntidade



class TarefasEntidade(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_entrega = models.DateTimeField()
    concluida = models.BooleanField()

    # Relacionamento com a entidade AlunosEntidade (chave estrangeira)
    alunos_tarefas = models.ForeignKey(AlunosEntidade, on_delete=models.CASCADE, blank=False, null=False)
    # Relacionamento com a entidade DisciplinasEntidade (muitos para muitos)
    disciplinas = models.ManyToManyField(DisciplinasEntidade)

    def __str__(self) -> str:
        return "Tarefas [%i - %s]" % (self.id, self.titulo)
