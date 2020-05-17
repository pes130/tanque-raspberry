from flask import Flask
from flask_cors import CORS, cross_origin
from flask import jsonify


app = Flask(__name__)
cors = CORS(app)
app.config["APPLICATION_ROOT"] = "/tank"
app.config['CORS_HEADERS'] = 'Content-Type'

from tanque import Tanque


motor1_pins = {"in1": 24,"in2": 23,"en": 25}
motor2_pins = {"in1": 22,"in2": 27,"en": 17}

tanque = Tanque(motor1_pins['en'], 
                motor1_pins['in1'], 
                motor1_pins['in2'],
                motor2_pins['en'], 
                motor2_pins['in1'], 
                motor2_pins['in2'])

@app.route('/')
def main():
    return jsonify(status=200,action="OK")

@app.route('/m/f')
def avanzar():
    tanque.avanzar()
    return jsonify(status=200,action="move forward")

@app.route('/m/s')
def parar():
    tanque.stop()
    return jsonify(status=200,action="stop")

@app.route('/m/l2')
def izquierda_rapido():
    tanque.giro_izq_2()
    return jsonify(status=200,action="left_fast")

@app.route('/m/l')
def izquierda():
    tanque.giro_izq_1()
    return jsonify(status=200,action="left")

@app.route('/m/r2')
def derecha_rapido():
    tanque.giro_der_2()
    return jsonify(status=200,action="right_fast")

@app.route('/m/r')
def derecha():
    tanque.giro_der_1()
    return jsonify(status=200,action="right")

@app.route('/m/b')
def retroceder():
    tanque.retroceder()
    return jsonify(status=200,action="backward")

@app.route('/m/v/<velocidad>')
def cambiar_velocidad(velocidad):
    print("Velocidad: ", velocidad)
    if velocidad == "alta":
        tanque.velocidad_alta()
        return jsonify(status=200,action="high speed")
    elif velocidad == "media":
        tanque.velocidad_media()
        return jsonify(status=200,action="mid speed")
    elif velocidad == "baja":
        tanque.velocidad_baja()
        return jsonify(status=200,action="low speed")
    return jsonify(status=400,action="Bad speed parameter")



if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")