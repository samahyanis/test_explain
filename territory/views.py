from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status

from . import models
from .serializers import TerritorySerializer, DepartementSerializer


@api_view(['GET'])
def get_departement(request):

    departement  = models.Terriotry.objects.filter(kind="FRDEPA")
    serializer = DepartementSerializer(departement,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_departement_by_name(request):

    try:

        name = request.query_params["deparement_name"]
        departement  = models.Terriotry.objects.get(name=name,kind="FRDEPA")


        serializer = TerritorySerializer(departement)
        return Response(serializer.data)

    except:
        return Response("Not found",status=status.HTTP_404_NOT_FOUND)
