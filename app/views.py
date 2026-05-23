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

def equipe (request):
    lista_personagens = [
        {
            'nome': 'Alex',
            'idade': '18',
            'posicao': 'Especialista em Esportes',
            'local': 'Beverly Hills',
            'imagem': 'app/img/alexelenco.png' 
        },
        {
            'nome': 'Clover',
            'idade': '18',
            'posicao': 'Especialista em Combate',
            'local': 'Beverly Hills',
            'imagem': 'app/img/cloverelenco.png' 
        },
        {
            'nome': 'Samantha (Sam)',
            'idade': '18',
            'posicao': 'Líder / Estrategista',
            'local': 'Beverly Hills',
            'imagem': 'app/img/samelenco.png' 
        },
        {
            'nome': 'Jerry Lewis',
            'idade': '60',
            'posicao': 'Fundador da WOOHP',
            'local': 'Londres',
            'imagem': 'app/img/jerryelenco.png' 
        },
    ]
    return render(request, 'app/equipe.html', {'elenco': lista_personagens})

def sobre(request):
    return render (request, 'app/sobre.html')
