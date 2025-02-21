from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

def hola_mundo(request):
    return HttpResponse("""
        <h1>hola mundo con Django!!</h1>
        <h3>Soy Víctor Vergara Web</h3>    
    """)