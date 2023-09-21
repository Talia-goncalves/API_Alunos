# Importando classes e módulos necessários do Django REST framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importando o modelo TarefasEntidade e o serializador SerializerTarefas
from ..models.tarefas import TarefasEntidade
from ..serializers.serializerTarefas import SerializerTarefas

# Criando uma classe chamada TarefasView que herda da classe APIView do Django REST framework
class TarefasView(APIView):
    # Método GET para buscar tarefas
    def get(self, request, id=None):
        # Verifica se um ID foi fornecido na URL
        if id is not None:
            try:
                # Tenta encontrar uma tarefa com o ID fornecido
                tarefas = TarefasEntidade.objects.get(pk=id)
                # Serializa a tarefa encontrada usando SerializerTarefas
                serializer = SerializerTarefas(tarefas, many=False)
                # Retorna os dados serializados como resposta
                return Response(serializer.data)
            except TarefasEntidade.DoesNotExist:
                # Retorna uma resposta de erro se a tarefa não existe
                return Response({'details': 'Tarefa não existe'}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            # Se nenhum ID foi fornecido, busca todas as tarefas
            tarefas = TarefasEntidade.objects.all()
            # Serializa a lista de tarefas usando SerializerTarefas
            serializer = SerializerTarefas(tarefas, many=True)
            # Retorna os dados serializados como resposta
            return Response(serializer.data)

    # Método POST para criar uma nova tarefa
    def post(self, request, format=None):
        # Serializa os dados recebidos na requisição usando SerializerTarefas
        serializer = SerializerTarefas(data=request.data)
        if serializer.is_valid():
            # Se os dados são válidos, salva a tarefa no banco de dados
            serializer.save()
            # Retorna os dados serializados como resposta com status de criação (201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Retorna uma resposta de erro se os dados não são válidos
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Método PUT para atualizar uma tarefa existente
    def put(self, request, id, format=None):
        try:
            # Tenta encontrar a tarefa com o ID fornecido
            tarefas = TarefasEntidade.objects.get(pk=id)
        except TarefasEntidade.DoesNotExist:
            # Retorna uma resposta de erro se a tarefa não existe
            return Response({'details': 'Tarefa não existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Serializa os dados recebidos na requisição usando SerializerTarefas
        serializer = SerializerTarefas(tarefas, data=request.data)
        if serializer.is_valid():
            # Se os dados são válidos, atualiza a tarefa no banco de dados
            serializer.save()
            # Retorna os dados serializados como resposta com status de criação (201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Retorna uma resposta de erro se os dados não são válidos
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Método DELETE para excluir uma tarefa
    def delete(self, request, id, format=None):
        # Tenta encontrar a tarefa com o ID fornecido
        try:
            tarefas = TarefasEntidade.objects.get(pk=id)
        except TarefasEntidade.DoesNotExist:
            # Retorna uma resposta de erro se a tarefa não existe
            return Response({'details': 'Tarefa não existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Exclui a tarefa do banco de dados
        tarefas.delete()
        # Retorna uma resposta de sucesso sem conteúdo (204) após a exclusão
        return Response(status=status.HTTP_204_NO_CONTENT)
