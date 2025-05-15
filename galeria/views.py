from django.shortcuts import render, get_object_or_404
from galeria.models import Photograph

def index(request):

    context = {
        "title": "Alura Space - Galeria",
        "cards": Photograph.objects.order_by('created_at').filter(published=True)
    }


    return render(request, "galeria/index.html", context)


def imagem(request, image_id):
    photograph = get_object_or_404(Photograph, pk=image_id)
    title = 'Alura Space - Imagens'

    context = {
        "photograph": photograph,
        "title": title
    }
    return render(request, "galeria/imagem.html", context)
