from rest_framework import serializers
from controleTarefas.models.disciplinas import DisciplinasEntidade

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = DisciplinasEntidade
        fields = '__all__'