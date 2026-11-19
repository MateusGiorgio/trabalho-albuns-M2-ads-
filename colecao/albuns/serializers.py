from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'

    def validate_avaliacao(self, valor):
        if valor < 0 or valor > 10:
            raise serializers.ValidationError(
                "A avaliação deve estar entre 0 e 10."
            )
        return valor

    def validate_ano(self, valor):
        if valor < 1900 or valor > 2026:
            raise serializers.ValidationError(
                "O ano deve estar entre 1900 e 2026."
            )
        return valor
