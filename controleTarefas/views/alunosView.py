# Importando classes e módulos necessários do Django REST framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importando o modelo de AlunosEntidade e o serializador AlunosSerializer
from controleTarefas.models.alunos import AlunosEntidade
from controleTarefas.serializers.serializerAlunos import AlunosSerializer

# Criando uma classe chamada AlunosView que herda da classe APIView do Django REST framework
class AlunosView(APIView):
    # Método GET para buscar alunos
    def get(self, request, pk=None):
        # Verifica se um ID foi fornecido na URL
        if pk is not None:
            try:
                # Tenta encontrar um aluno com o ID fornecido
                alunos = AlunosEntidade.objects.get(pk=pk)
                # Serializa o aluno encontrado usando AlunosSerializer
                serializer = AlunosSerializer(alunos, many=False)
                # Retorna os dados serializados como resposta
                return Response(serializer.data)
            except AlunosEntidade.DoesNotExist:
                # Retorna uma resposta de erro se o aluno não existe
                return Response({'details': 'Aluno não existe'}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            # Se nenhum ID foi fornecido, busca todos os alunos
            alunos = AlunosEntidade.objects.all()
            # Serializa a lista de alunos usando AlunosSerializer
            serializer = AlunosSerializer(alunos, many=True)
            # Retorna os dados serializados como resposta
            return Response(serializer.data)

    # Método POST para criar um novo aluno
    def post(self, request, format=None):
        # Serializa os dados recebidos na requisição usando AlunosSerializer
        serializer = AlunosSerializer(data=request.data)
        if serializer.is_valid():
            # Se os dados são válidos, salva o aluno no banco de dados
            serializer.save()
            # Retorna os dados serializados como resposta com status de criação (201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Retorna uma resposta de erro se os dados não são válidos
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Método PUT para atualizar um aluno existente
    def put(self, request, pk, format=None):
        try:
            # Tenta encontrar o aluno com o ID fornecido
            alunos = AlunosEntidade.objects.get(pk=pk)
        except AlunosEntidade.DoesNotExist:
            # Retorna uma resposta de erro se o aluno não existe
            return Response({'details': 'Aluno não existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Serializa os dados recebidos na requisição usando AlunosSerializer
        serializer = AlunosSerializer(alunos, data=request.data)
        if serializer.is_valid():
            # Se os dados são válidos, atualiza o aluno no banco de dados
            serializer.save()
            # Retorna os dados serializados como resposta com status de criação (201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Retorna uma resposta de erro se os dados não são válidos
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Método DELETE para excluir um aluno
    def delete(self, request, pk, format=None):
        # Tenta encontrar o aluno com o ID fornecido
        try:
            alunos = AlunosEntidade.objects.get(pk=pk)
        except AlunosEntidade.DoesNotExist:
            # Retorna uma resposta de erro se o aluno não existe
            return Response({'details': 'Aluno não existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Exclui o aluno do banco de dados
        alunos.delete()
        # Retorna uma resposta de sucesso sem conteúdo (204) após a exclusão
        return Response(status=status.HTTP_204_NO_CONTENT)
