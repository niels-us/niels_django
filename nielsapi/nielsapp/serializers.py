from asyncio.windows_events import NULL
from rest_framework import serializers
from .models import Usuario, Equipo, Integrante
from drf_extra_fields.fields import Base64ImageField


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class EquipoSerializer(serializers.ModelSerializer):    
    imagen = Base64ImageField(required=False)
    class Meta:
        model = Equipo
        fields = '__all__'


class IntegranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integrante
        fields = '__all__'


class DescIntegranteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Integrante
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'usuario': instance.usuario.nombre,
            'equipo': instance.equipo.nombre,
            # 'foto_equipo': instance.equipo.imagen if instance.equipo.imagen != '' else '',
            'fecha_ingreso': instance.fecha,
        }

class CountIntegranteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Integrante
        fields = '__all__'

    def to_representation(self, instance):
        return{
            # 'usuario': instance.usuario.nombre,
            'equipo': instance.equipo.nombre,
        }

# import base64, uuid
# from django.core.files.base import ContentFile


# # Custom image field - handles base 64 encoded images
# class Base64ImageField(serializers.ImageField):
#     def to_internal_value(self, data):
#         if isinstance(data, str) and data.startswith('data:image'):
#             # base64 encoded image - decode
#             format, imgstr = data.split(';base64,') # format ~= data:image/X,
#             ext = format.split('/')[-1] # guess file extension
#             id = uuid.uuid4()
#             data = ContentFile(base64.b64decode(imgstr), name = id.urn[9:] + '.' + ext)
#         return super(Base64ImageField, self).to_internal_value(data)
