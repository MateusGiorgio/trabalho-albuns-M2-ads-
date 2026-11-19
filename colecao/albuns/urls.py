
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, resumo_albuns
from .views import AlbumViewSet, resumo_albuns, pesquisar_albuns

router = DefaultRouter()
router.register(r'albuns', AlbumViewSet, basename='album')

urlpatterns = [
    path('albuns/resumo/', resumo_albuns),
    path('albuns/pesquisar/', pesquisar_albuns),
] + router.urls
