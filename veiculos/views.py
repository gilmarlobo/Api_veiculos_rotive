from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Veiculo
from .serializers import VeiculoSerializer

@api_view(['GET'])
def get_veiculo(request, placa):
    try:
        veiculo = Veiculo.objects.get(placa=placa.upper())
        serializer = VeiculoSerializer(veiculo)
        return Response(serializer.data)
    except Veiculo.DoesNotExist:
        return Response({"error": "Veículo não encontrado seu mané, ta vendo a lista de veículos ai não?"}, status=404)