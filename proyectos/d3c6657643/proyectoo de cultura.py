pip install flask

from flask import Flask, render_template

app = Flask(__name__)

# Datos de las progresiones
progresiones = [
    {
        "titulo": "Progresión 1",
        "descripcion": "Descripción de la progresión 1."
    },
    {
        "titulo": "Progresión 2",
        "descripcion": "Descripción de la progresión 2."
    },
    {
        "titulo": "Progresión 3",
        "descripcion": "Descripción de la progresión 3."
    },
    {
        "titulo": "Progresión 4",
        "descripcion": "Descripción de la progresión 4."
    },
    {
        "titulo": "Progresión 5",
        "descripcion": "Descripción de la progresión 5."
    },
    {
        "titulo": "Progresión 6",
        "descripcion": "Descripción de la progresión 6."
    },
    {
        "titulo": "Progresión 7",
        "descripcion": "Descripción de la progresión 7."
    }
]

# Rutas
@app.route('/')
def index():
    return render_template('index.html', progresiones=progresiones)

if __name__ == '__main__':
    app.run(debug=True)





<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cultura Digital II</title>
</head>
<body>
    <header>
        <h1>Cultura Digital II</h1>
    </header>
    <div class="container">
        {% for progresion in progresiones %}
        <div class="progression">
            <h2>{{ progresion['titulo'] }}</h2>
            <p>{{ progresion['descripcion'] }}</p>
            <!-- Aquí puedes añadir más contenido para cada progresión -->
        </div>
        {% endfor %}
    </div>
</body>
</html>
