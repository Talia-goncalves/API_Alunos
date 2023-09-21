from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.alunos import AlunosEntidade
from ..models.tarefas import TarefasEntidade
from ..serializers.serializerTarefas import SerializerTarefas

class AlunoTarefasView(APIView):
    def get (self, request, id):
        try:
            #Busca o aluno pelo ID try:
            alunos = AlunosEntidade.objects.get(pk=id)
        except alunos.DoesNotExist:
            return Response({'details': 'Tarefa não existe'}, status=status.HTTP_400_BAD_REQUEST)
        #Retorna todas tarefa com esse ID associado
        tarefas = TarefasEntidade.objects. filter (aluno_delegado=alunos)
        serializer = SerializerTarefas (tarefas, many=True)
        return Response(serializer .data)