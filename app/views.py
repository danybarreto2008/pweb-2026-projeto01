from django.shortcuts import render
from .models import Serie, Personagem, SobreInfo

def inicio(request):
    serie = Serie.objects.first()
    return render(request, 'app/inicio.html', {'serie': serie})

def equipe(request):
    elenco = Personagem.objects.all()
    return render(request, 'app/equipe.html', {'elenco': elenco})

def sobre(request):
    info = SobreInfo.objects.first()
    return render(request, 'app/sobre.html', {'info': info})
