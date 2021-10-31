import base64
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Equipo, Usuario, Integrante
from .serializers import EquipoSerializer, UsuarioSerializer, IntegranteSerializer, DescIntegranteSerializer
import asyncio


# Create your views here.

@api_view(['GET'])
def index(request):
    """ Benvenida  """
    data = {'mensaje': 'Bienvenido a Gestion de Equipos'}
    return Response(data)

# CRUD EQUIPO *******************************************************************


@api_view(['GET'])
def DetEquipo(request):
    equipos = Equipo.objects.all()
    serializer = EquipoSerializer(equipos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Equipos(request, pk=None):
    # select
    if request.method == 'GET':
        equipo = Equipo.objects.filter(id=pk).first()
        serializer = EquipoSerializer(equipo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # insert
    elif request.method == 'POST':
        serializer = EquipoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # ENVIA CORREO CUANDO SE CREA UN EQUIPO
        asyncio.run(email('POST', request.data['nombre']))

        nuevoEquipo = serializer.save()
        return Response(EquipoSerializer(nuevoEquipo).data, status=status.HTTP_201_CREATED)
    # update
    elif request.method == 'PUT':
        equipo = Equipo.objects.filter(id=pk).first()
        serializer = EquipoSerializer(equipo, data=request.data)
        serializer.is_valid(raise_exception=True)
        nuevoEquipo = serializer.save()
        return Response(EquipoSerializer(nuevoEquipo).data, status=status.HTTP_200_OK)
    # delete
    elif request.method == 'DELETE':
        equipo = Equipo.objects.filter(id=pk).first()
        equipo.delete()
        return Response({'message': 'Equipo Eliminado correctamente!'}, status=status.HTTP_200_OK)

# CRUD USUARIO *******************************************************************


@api_view(['GET'])
def DetUsuario(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Usuarios(request, pk=None):
    # select
    if request.method == 'GET':
        usuario = Usuario.objects.filter(id=pk).first()
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # insert
    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        nuevoUsuario = serializer.save()
        return Response(UsuarioSerializer(nuevoUsuario).data, status=status.HTTP_201_CREATED)
    # update
    elif request.method == 'PUT':
        usuario = Usuario.objects.filter(id=pk).first()
        serializer = UsuarioSerializer(usuario, data=request.data)
        serializer.is_valid(raise_exception=True)
        nuevoUsuario = serializer.save()
        return Response(UsuarioSerializer(nuevoUsuario).data, status=status.HTTP_200_OK)
    # delete
    elif request.method == 'DELETE':
        usuario = Usuario.objects.filter(id=pk).first()
        usuario.delete()
        return Response({'message': 'Usuario Eliminado correctamente!'}, status=status.HTTP_200_OK)

# CRUD INTEGRANTE *******************************************************************


@api_view(['GET'])
def DetIntegrante(request):
    integrantes = Integrante.objects.all()
    serializer = IntegranteSerializer(integrantes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Integrantes(request, pk=None):
    # select
    if request.method == 'GET':
        integrante = Integrante.objects.filter(id=pk).first()
        serializer = IntegranteSerializer(integrante)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # insert
    elif request.method == 'POST':
        serializer = IntegranteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        nuevoIntegrante = serializer.save()
        return Response(IntegranteSerializer(nuevoIntegrante).data, status=status.HTTP_201_CREATED)
    # update
    elif request.method == 'PUT':
        integrante = Integrante.objects.filter(id=pk).first()
        serializer = IntegranteSerializer(integrante, data=request.data)
        serializer.is_valid(raise_exception=True)
        nuevoIntegrante = serializer.save()
        return Response(IntegranteSerializer(nuevoIntegrante).data, status=status.HTTP_200_OK)
    # delete
    elif request.method == 'DELETE':
        integrante = Integrante.objects.filter(id=pk).first()
        integrante.delete()
        return Response({'message': 'integrante Eliminado correctamente!'}, status=status.HTTP_200_OK)

# CRUD INTEGRANTE EQUIPO USUARIO *******************************************************************

@api_view(['GET'])
def DescEquipo(request):
    integrantes = Integrante.objects.all()
    serializer = DescIntegranteSerializer(integrantes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




# CALCULAR CANTIDAD DE INTEGRANTES POR GRUPO


def NumIntegrante(request):
    integrantes = Integrante.objects.all()
    serializer = IntegranteSerializer(integrantes, many=True)
    print(serializer.data)
    return Response('LISTO')


# CORREO


async def email(request, nomEquipo):
    subject = 'Felicidades se creo el Equipo ' + nomEquipo
    message = 'Agregale usuario al equipo ' + nomEquipo
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['nilstar80@gmail.com', ]
    send_mail(subject, message, email_from, recipient_list)
    return 'listo'


# base 64

# with open('mn.png', 'rb') as imagefile:
#     byteform=base64.b64encode(imagefile.read())

# f=open('output.bin','wb')
# f.write(byteform)
# f.close()

# file=open('output.bin', 'rb')
# byte=file.read()
# file.close()

# fh= open('mab.png', 'wb')
# fh.write(base64.b64decode((byte)))
# fh.close()


# def base64Imagen():
# print(base64.b64decode('hola') , ' base64')
