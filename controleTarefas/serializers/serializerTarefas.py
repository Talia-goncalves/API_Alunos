from rest_framework import serializers
from ..models.tarefas import TarefasEntidade

class SerializerTarefas(serializers.ModelSerializer):
    class Meta: 
        modelo = TarefasEntidade
        fields = '__all__'