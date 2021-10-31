from rest_framework import serializers
from .models import Usuario, Equipo, Integrante
import base64, uuid

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

    # def imagen(self, place):
    #     imagen = open( self.imagen.path, "rb") 
    #     data = imagen.read() 
    #     return "data:image/jpg;base64,%s" % data.encode('base64')

# INTEGRANTE******************************************************************************


class IntegranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integrante
        fields = '__all__'

# DESCRIPCION INTEGRANTE******************************************************************************


class DescIntegranteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Integrante
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'usuario': instance.usuario.nombre,
            'equipo': instance.equipo.nombre,
            'foto_equipo': instance.equipo.imagen if instance.equipo.imagen != '' else '',
            'fecha_ingreso': instance.fecha,

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