from rest_framework import serializers
from .models import Veiculo

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['placa', 'marca', 'modelo', 'ano', 'cambio', 'cor', 'combustivel']