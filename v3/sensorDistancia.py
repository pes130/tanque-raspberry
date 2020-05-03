import RPi.GPIO as GPIO 
import time 
#set GPIO Pins 
GPIO_TRIGGER = 2 
GPIO_ECHO = 3


class SensorDistancia:
    def __init__(self, pin_trigger, pin_echo):
        self._trigger = pin_trigger
        self._echo = pin_echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._trigger, GPIO.OUT) 
        GPIO.setup(self._echo, GPIO.IN) 

    '''
    Distancia en cm
    '''
    def distancia(self): 
        GPIO.output(self._trigger, GPIO.HIGH) 
        time.sleep(0.00001) 			
        GPIO.output(self._trigger, GPIO.LOW) 
        while GPIO.input(self._echo) == 0: 
            inicioEcho = time.time() 
        while GPIO.input(self._echo) == 1: 
            finEcho = time.time() 
        tiempoTranscurrido = finEcho - inicioEcho 
        # multiplicas por la velocidad del sonido (34300 cm/s) entre 2 porque es ida y vuelta
        distance = (tiempoTranscurrido * 34300) / 2 
        return distance 

    def __destroy__(self):
        GPIO.cleanup()


if __name__ == '__main__':
    sensorDistancia = SensorDistancia(2, 3)

    while True: 
        dist = sensorDistancia.distancia() 
        print("Distancia = ",dist," cm")
        time.sleep(1)


