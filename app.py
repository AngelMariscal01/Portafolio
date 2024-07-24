from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/experiencia')
def experiencia():
    return render_template('experiencia.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/proyectoUno')
def proyectoUno():
    return render_template('proyectoUno.html')

@app.route('/proyectoDos')
def proyectoDos():
    return render_template('proyectoDos.html')

@app.route('/proyectoTres')
def proyectoTres():
    return render_template('proyectoTres.html')

@app.route('/proyectoCuatros')
def proyectoCuatros():
    return render_template('proyectoCuatros.html')

@app.route('/logros')
def logros():
    return render_template('logros.html')

@app.route('/habilidades')
def habilidades():
    return render_template('habilidades.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')


if __name__ == '__main__':
    app.run(debug=True)
