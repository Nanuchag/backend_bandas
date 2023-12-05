from django.shortcuts import render
from django.http import HttpResponse

from app.models import Banda

from app import serializers

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


# Create your views here.
def index(request):
    return HttpResponse('<h1> Hola mundo Django! 🦄</h1>')

@api_view(['GET'])
def get_band(request):
    #LISTA DE TODAS LAS BANDAS

    #SE BUSCA TODOS LOS REGISTROS GUARDADOS EN LA BASE
    banda = Banda.objects.all() 
    #CUANDO ESTÁS SERIALIZANDO MULTIPLES INSTANCIAS DE UN MODELO
    serializer = serializers.BandaSerializer(banda, many=True)
    #RESPONSE ES UNA CLASE QUE ME PERMITE DEVOLVER UNA RESPUESTA
    #QUE CUMPLE CON LOS ESTANDARES DE API-REST
    return Response(serializer.data)

@api_view(['POST'])
def create_band(request):
    #SE CREA LOS DATOS RECIBIDOS DESDE EL FORMULARIO
    serializer = serializers.BandaSerializer(data=request.data)
    #SE EJECUTAN LAS VALIDACIONES
    if serializer.is_valid():
        #SE REGISTRA EN BASE DE DATOS
        serializer.save()
        #SE GENERA LA RESPUESTA QUE SE DEVUELVE
        response = { 'status': 'Ok',
                    'message':'Registro guardado correctamente',
                    'data': serializer.data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    response = {'status': 'Error',
                'message': 'No se pudo crear la banda',
                 'errors': serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detail_band(request, id):
    #MUESTRA UNA BANDA
    try:
        #SE BUSCA LA BANDA EN BASE POR EL ID
        banda = Banda.objects.get(pk=id)
    except Banda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Recurso no existe')
    
    serializer = serializers.BandaSerializer(banda)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_band(request, id):
    #ELIMINA UNA BANDA
    try:
        banda = Banda.objects.get(pk=id)
    except Banda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Recurso no existe')
    #SE ELIMINA LA BANDA EN BASE DE DATOS
    banda.delete()
    return Response({'message': 'Se elimino la banda'}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_band(request, id):
    #ACTUALIZA UNA BANDA

    try:
        banda = Banda.objects.get(pk=id)
    except Banda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data= 'Recurso no existe')
    
    serializer = serializers.BandaSerializer(banda, data=request, )
    if serializer.is_valid():
        serializer.save()
        response = {'status': 'Ok'
                    ,'message':'Actualizado Correctamente',
                    'data': serializer.data}
        return Response(data=response)
    #NO SE CUMPLE LA VALIDACION
    response = {'status': 'Error',
                'message': 'No se pudo modificar la banda',
                'errors': serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)



# def delete_band(request):
#  return HttpResponse('<h1> Se elimino la banda</h1>')