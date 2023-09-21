from rest_framework import serializers
from controleTarefas.models.disciplinas import DisciplinasEntidade

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta: 
        modelo = DisciplinasEntidade
        fields = '__all__'