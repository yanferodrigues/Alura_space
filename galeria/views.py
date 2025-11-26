from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by('horario').filter(publicado = True)
    return render(request, 'galeria/index.html',{'cards':fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia,pk=foto_id )
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by('horario').filter(publicado = True)
    
    if 'buscar' in request.GET:
        nome_busca = request.GET['buscar']
        if nome_busca:
            fotografias = fotografias.filter(nome__icontains= nome_busca)
    
    return render(request,'galeria/busca.html',{'cards':fotografias})