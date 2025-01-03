from django.shortcuts import render


def index(request):
    # Adiciona 'range_values' no contexto para o template
    return render(request, 'galeria/index.html', {'range_values': range(6)})


def imagem(request):
    return render(request, 'galeria/imagem.html')
