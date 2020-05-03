from time import sleep
from tanque import Tanque


motor1_pins = {
    "in1": 24,
    "in2": 23,
    "en": 25
}

motor2_pins = {
    "in1": 22,
    "in2": 27,
    "en": 17
}


tanque = Tanque(motor1_pins['en'], 
                motor1_pins['in1'], 
                motor1_pins['in2'],
                motor2_pins['en'], 
                motor2_pins['in1'], 
                motor2_pins['in2'])

print('''
CONTROL DEL TANQUE
------------------
w - hacia adelante
s - hacia atrás
a - giro izquierda suave
d - giro derecha suave
q - giro izquierda rápido
e - giro derecha rápido

1 - velocidad baja
2 - velocidad media
3 - velocidad alta
espacio - stop

0 - salir
''')

orden="-1"

while orden!="0":

    orden = input(">: ")
    
    if orden==" ":
        tanque.stop()

    elif orden=="w":
        tanque.avanzar()

    elif orden=="s":
        tanque.retroceder()

    elif orden=="a":
        tanque.giro_izq_1()
    
    elif orden=="d":
        tanque.giro_der_1()

    elif orden=="q":
        tanque.giro_izq_2()
    
    elif orden=="e":
        tanque.giro_der_2()

    elif orden=="1":
        tanque.velocidad_baja()

    elif orden=="2":
        tanque.velocidad_media()

    elif orden=="3":
        tanque.velocidad_alta()

print("Fin")