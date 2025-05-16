from django.urls import path
from galeria.views import index, imagem, search, filter

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:image_id>', imagem, name='imagem'),
    path('search/', search, name='search'),
    path('filter/', filter, name='filter'),
]