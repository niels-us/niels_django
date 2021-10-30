from rest_framework import serializers
from .models import Usuario, Equipo, Integrante

# USUARIO******************************************************************************


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

# EQUIPO******************************************************************************


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'

# INTEGRANTE******************************************************************************


class IntegranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integrante
        fields = '__all__'
