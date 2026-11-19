
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Album
from .serializers import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


@api_view(['GET'])
def resumo_albuns(request):
    albuns = Album.objects.all()

    total = len(albuns)
    soma = 0
    melhor = None

    for album in albuns:
        soma += album.avaliacao

        if melhor is None or album.avaliacao > melhor.avaliacao:
            melhor = album

    if total > 0:
        media = round(soma / total, 2)
        melhor_album = melhor.titulo
    else:
        media = 0
        melhor_album = None

    return Response({
        "total": total,
        "media_avaliacao": media,
        "melhor": melhor_album
    })

@api_view(['GET'])
def pesquisar_albuns(request):
    busca = request.query_params.get('q', '')

    albuns = Album.objects.filter(
        Q(titulo__icontains=busca) |
        Q(artista__icontains=busca)
    )

    serializer = AlbumSerializer(albuns, many=True)

    return Response(serializer.data)