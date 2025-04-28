from flask import Flask

app = Flask(__name__)

#Crear ruta Flask
@app.route('/')
def index():
    return "Aprendiendo Flask con Víctor Vergara"

@app.route('/informacion')
def informacion():
    return "<h1>Página de información</h1>"

@app.route('/contacto')
def contacto():
    return "<h1>Página de contacto</h1>"

@app.route('/lenguajes-de-programacion')
def lenguajes():
    return "<h1>Página de lenguajes</h1>"

if __name__ == '__main__':
    app.run(debug=True)
