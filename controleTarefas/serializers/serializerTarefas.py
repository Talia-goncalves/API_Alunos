from rest_framework import serializers
from controleTarefas.models.tarefas import TarefasEntidade

class SerializerTarefas(serializers.ModelSerializer):
    class Meta: 
        model = TarefasEntidade
        fields = '__all__'