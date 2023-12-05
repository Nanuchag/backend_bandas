from rest_framework import serializers
from app.models import Banda

class BandaSerializer(serializers.ModelSerializer):
    artistas = serializers.StringRelatedField(many=True)

    class Meta:
        model = Banda
        fields = ['id', 'artist', 'release_date', 'price', 'perfil']