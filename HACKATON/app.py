from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    # Esta función carga la página web por primera vez
    return render_template('juego.html', mensaje="¿Qué emoción representa este pictograma? 🤔")

@app.route('/comprobar', methods=['POST'])
def comprobar():
    # Aquí llega la respuesta cuando el usuario pulsa un botón
    boton_pulsado = request.form.get('emocion')
    
    # La respuesta correcta es Alegría (porque mostraremos una cara sonriente)
    if boton_pulsado == "Alegria":
        resultado = "¡Correcto! 🎉 La comunicación visual nos ayuda a entendernos mejor."
    else:
        resultado = "¡Casi! Intentándolo de nuevo seguro que lo aciertas. 💪"
        
    return render_template('juego.html', mensaje=resultado)

if __name__ == '__main__':
    app.run(debug=True)