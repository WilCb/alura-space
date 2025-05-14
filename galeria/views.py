from django.shortcuts import render


def index(request):
    title = 'Alura Space - Galeria'
    return render(request, 'galeria/index.html', {'title': title})

def imagem(request):
    title = 'Alura Space - Imagem'
    return render(request, 'galeria/imagem.html', {'title': title})