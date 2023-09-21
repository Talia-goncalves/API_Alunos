# Importando classes e módulos necessários do Django REST framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importando o modelo DisciplinasEntidade e o serializador DisciplinaSerializer
from controleTarefas.models.disciplinas import DisciplinasEntidade
from controleTarefas.serializers.serializerDisciplinas import DisciplinaSerializer

# Criando uma classe chamada DisciplinasView que herda da classe APIView do Django REST framework
class DisciplinasView(APIView):
    # Método GET para buscar disciplinas
    def get(self, request, pk=None):
        # Verifica se um ID foi fornecido na URL
        if id is not None:
            try:
                # Tenta encontrar uma disciplina com o ID fornecido
                disciplinas = DisciplinasEntidade.objects.get(pk=pk)
                # Serializa a disciplina encontrada usando DisciplinaSerializer
                serializer = DisciplinaSerializer(disciplinas, many=False)
                # Retorna os dados serializados como resposta
                return Response(serializer.data)
            except DisciplinasEntidade.DoesNotExist:
                # Retorna uma resposta de erro se a disciplina não existe
                return Response({'details': 'Disciplina não existe'}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            # Se nenhum ID foi fornecido, busca todas as disciplinas
            disciplinas = DisciplinasEntidade.objects.all()
            # Serializa a lista de disciplinas usando DisciplinaSerializer
            serializer = DisciplinaSerializer(disciplinas, many=True)
            # Retorna os dados serializados como resposta
            return Response(serializer.data)

    # Método POST para criar uma nova disciplina
    def post(self, request, format=None):
        # Serializa os dados recebidos na requisição usando DisciplinaSerializer
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            # Se os dados são válidos, salva a disciplina no banco de dados
            serializer.save()
            # Retorna os dados serializados como resposta com status de criação (201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Retorna uma resposta de erro se os dados não são válidos
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Método PUT para atualizar uma disciplina existente
    def put(self, request, pk, format=None):
        try:
            # Tenta encontrar a disciplina com o ID fornecido
            disciplinas = DisciplinasEntidade.objects.get(pk=pk)
        except DisciplinasEntidade.DoesNotExist:
            # Retorna uma resposta de erro se a disciplina não existe
            return Response({'details': 'Disciplina não existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Serializa os dados recebidos na requisição usando DisciplinaSerializer
        serializer = DisciplinaSerializer(disciplinas, data=request.data)
        if serializer.is_valid():
            # Se os dados são válidos, atualiza a disciplina no banco de dados
            serializer.save()
            # Retorna os dados serializados como resposta com status de criação (201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Retorna uma resposta de erro se os dados não são válidos
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Método DELETE para excluir uma disciplina
    def delete(self, request, pk, format=None):
        # Tenta encontrar a disciplina com o ID fornecido
        try:
            disciplinas = DisciplinasEntidade.objects.get(pk=pk)
        except DisciplinasEntidade.DoesNotExist:
            # Retorna uma resposta de erro se a disciplina não existe
            return Response({'details': 'Disciplina não existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Exclui a disciplina do banco de dados
        disciplinas.delete()
        # Retorna uma resposta de sucesso sem conteúdo (204) após a exclusão
        return Response(status=status.HTTP_204_NO_CONTENT)
