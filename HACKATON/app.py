from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

sonido_activado = False

# 1. Ruta para la primera pantalla (Menú)
@app.route('/')
def inicio():
    return render_template('juego.html')

# 2. Ruta para la segunda pantalla (Historia)
@app.route('/intro')
def historia():
    return render_template('intro.html')

# Guardar la opción del sonido
@app.route('/guardar_tts', methods=['POST'])
def guardar_tts():
    global sonido_activado
    datos = request.get_json()
    sonido_activado = datos.get('tts_activo')
    print("¿Sonido activado?:", sonido_activado)
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True)