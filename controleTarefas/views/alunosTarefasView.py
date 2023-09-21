from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from controleTarefas.models.alunos import AlunosEntidade
from controleTarefas.models.tarefas import TarefasEntidade
from controleTarefas.serializers.serializerTarefas import SerializerTarefas

class AlunoTarefasView(APIView):
    def get (self, request, pk):
        try:
            #Busca o aluno pelo ID try:
            alunos = AlunosEntidade.objects.get(pk=pk)
        except AlunosEntidade.DoesNotExist:
            return Response({'details': 'Tarefa não existe'}, status=status.HTTP_400_BAD_REQUEST)
        #Retorna todas tarefa com esse ID associado
        tarefas = TarefasEntidade.objects. filter(alunos_tarefas=alunos)
        serializer = SerializerTarefas (tarefas, many=True)
        return Response(serializer .data)