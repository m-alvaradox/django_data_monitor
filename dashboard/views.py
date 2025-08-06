from django.shortcuts import render
import requests
from django.conf import settings
from collections import Counter
from datetime import datetime

# Create your views here.

def index(request):

    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON

    # Número total de respuestas
    total_responses = len(posts)

  
    votes = Counter()   # Contar votos por productID
    timestamps = []

    for post in posts.values():
        product_id = post.get('productID')
        if product_id:
            votes[product_id] += 1

        # Convertir la fecha si existe
        date_str = post.get('date') or post.get('timestamp')
        if date_str:
            try:
                # ISO format
                timestamps.append(datetime.fromisoformat(date_str.replace("Z", "")))
            except ValueError:
                # Formato 29/07/2025, 08:13:12 p. m.
                try:
                    timestamps.append(datetime.strptime(date_str, "%d/%m/%Y, %I:%M:%S %p"))
                except:
                    pass  # Fecha inválida

    # Producto más votado
    most_voted_product = votes.most_common(1)[0] if votes else ('Ninguno', 0)
    last_vote = max(timestamps) if timestamps else None

    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
        'most_voted_product': most_voted_product[0],
        'last_vote': last_vote.strftime("%d/%m/%Y, %I:%M:%S %p") if last_vote else "No hay votos",
    }
        
    return render(request, "dashboard/index.html", data)
