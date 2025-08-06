from django.shortcuts import render
import requests
from django.conf import settings
from collections import Counter
from datetime import datetime

# Create your views here.

def index(request):

    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON
    conteos = posts

    # Número total de votos
    total_responses = sum(conteos.values())

    ordenado = sorted(conteos.items(), key=lambda x: x[1], reverse=True)
    plato_mas_popular = ordenado[0][0]
    votos_maximos = ordenado[0][1]

    plato_menos_popular = ordenado[-1][0]


    data = {
        'title': "La Tonga Manaba Dashboard",
        'total_responses': total_responses,
        'plato_mas_popular': plato_mas_popular,
        'votos_maximos': votos_maximos,
        'plato_menos_popular': plato_menos_popular,
    }
        
    return render(request, "dashboard/index.html", data)
