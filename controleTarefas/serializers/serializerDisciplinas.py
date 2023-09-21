from rest_framework import serializers
from ..models.disciplinas import DisciplinasEntidade

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta: 
        modelo = DisciplinasEntidade
        fields = '__all__'