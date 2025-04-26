from flask import Flask

app = Flask(__name__)

#Crear ruta Flask
@app.route('/')
def index():
    return "Aprendiendo Flask con Víctor Vergara"

if __name__ == '__main__':
    app.run(debug=True)
