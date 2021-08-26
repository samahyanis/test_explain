from rest_framework import serializers

from . import models
from .models import Terriotry, TerritorysParents


class DepartementSerializer(serializers.ModelSerializer):


    class Meta:
        model = Terriotry
        fields = ("__all__")




class CommuneSerializer(serializers.ModelSerializer):


    class Meta:
        model = Terriotry
        fields = ("__all__")


class EpciSerializer(serializers.ModelSerializer):
    commune = serializers.SerializerMethodField(source="get_commune")



    def get_commune(self, obj):
        epci = models.TerritorysParents.objects.filter(parent_id=obj.id)

        for x in epci:
            commune = Terriotry.objects.filter(id=x.child_id,kind="FRCOMM")
            if commune:
             yield CommuneSerializer(commune,many=True).data
    class Meta:
        model = Terriotry
        fields = ("__all__")



class TerritorySerializer(serializers.ModelSerializer):


    epci = serializers.SerializerMethodField(source="get_epci")

    def get_epci(self, obj):
        epci = models.TerritorysParents.objects.filter(parent_id=obj.id)

        for x in epci:
            Epci = Terriotry.objects.filter(id=x.child_id,kind="FREPCI")

            if Epci:
             yield EpciSerializer(Epci,many=True).data

    class Meta:
        model = Terriotry
        fields = ("__all__")





