from time import sleep
from motor import Motor


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


motor1 = Motor(motor1_pins['en'], motor1_pins['in1'], motor1_pins['in2'])
motor2 = Motor(motor2_pins['en'], motor2_pins['in1'], motor2_pins['in2'])

print('''
CONTROL DEL TANQUE
------------------
w - hacia adelante
s - hacia atrás

1 - velocidad baja
2 - velocidad media
3 - velocidad alta
espacio - stop

0 - salir
''')

orden="-1"

while orden!="0":

    x = input(">: ")
    
    if x==" ":
        motor1.stop()
        motor2.stop()

    elif x=="w":
        motor1.avanzar()
        motor2.avanzar()

    elif x=="s":
        motor1.retroceder()
        motor2.retroceder()

    elif x=="1":
        motor1.velocidad_baja()
        motor2.velocidad_baja()

    elif x=="2":
        motor1.velocidad_media()
        motor2.velocidad_media()

    elif x=="3":
        motor1.velocidad_alta()
        motor2.velocidad_alta()

    elif x=="4":
        motor1.velocidad_top()
        motor2.velocidad_top()

print("Fin")