# Importando classes e módulos necessários do Django REST framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importando os modelos AlunosEntidade e TarefasEntidade
from controleTarefas.models.alunos import AlunosEntidade
from controleTarefas.models.tarefas import TarefasEntidade

# Importando o serializador SerializerTarefas
from controleTarefas.serializers.serializerTarefas import SerializerTarefas

# Criando uma classe chamada AlunoTarefasView que herda da classe APIView do Django REST framework
class AlunoTarefasView(APIView):
    def get(self, request, pk):
        try:
            # Tenta buscar o aluno pelo ID
            aluno = AlunosEntidade.objects.get(pk=pk)
        except AlunosEntidade.DoesNotExist:
            # Retorna uma resposta de erro se o aluno não existe
            return Response({'details': 'Aluno não existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Busca todas as tarefas associadas a esse aluno
        tarefas = TarefasEntidade.objects.filter(alunos_tarefas=aluno)
        
        # Serializa a lista de tarefas usando SerializerTarefas
        serializer = SerializerTarefas(tarefas, many=True)
        
        # Retorna os dados serializados como resposta
        return Response(serializer.data)
