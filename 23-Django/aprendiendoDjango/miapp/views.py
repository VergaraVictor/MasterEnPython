from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

layout = """
<h1>Sitio web con Django | Víctor Vergara</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Página de pruebas</a>
    </li>
</ul>
<hr/>
"""

def index(request):

    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    """
    year = 2025
    while year <= 2050:

        if year %2 ==0:
            html += f"<li>{str(year)}</li>"
            
        year += 1

    html += "</ul>"

    return HttpResponse(layout+html)

def hola_mundo(request):
    return HttpResponse(layout+"""
        <h1>hola mundo con Django!!</h1>
        <h3>Soy Víctor Vergara Web</h3>    
    """)

def pagina(request):
    return HttpResponse(layout+"""
        <h1>Página de mi web</h1>
        <p>Creado por víctor Robles</p>
    """)