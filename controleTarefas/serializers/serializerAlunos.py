from rest_framework import serializers
from controleTarefas.models.alunos import AlunosEntidade

class AlunosSerializer(serializers.ModelSerializer):
    class Meta: 
        modelo = AlunosEntidade
        fields = '__all__'
