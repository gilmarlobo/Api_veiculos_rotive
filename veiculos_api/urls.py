from django.contrib import admin
from django.urls import path
from veiculos.views import get_veiculo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('veiculos_rotive/<str:placa>/', get_veiculo),
]