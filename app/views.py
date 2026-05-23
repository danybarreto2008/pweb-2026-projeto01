from django.shortcuts import render

def inicio (request):
    dados_serie = {
        'nome': 'Totally Spies!',
        'estreia': '2001',
        'genero': 'Ação, Aventura, Comédia e Espionagem',
        'publico': 'Infantil e Adolescente',
        'estilo': 'Inspirado em filmes de espionagem como 007.'
    }
    return render (request, 'app/inicio.html', {'serie': dados_serie})

def equipe(request):
    return render(request, 'app/equipe.html')

def sobre(request):
    return render (request, 'app/sobre.html')
