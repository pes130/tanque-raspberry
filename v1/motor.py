import RPi.GPIO as GPIO          

class Motor:
    LOW = 25
    MID = 50
    HIG = 75
    ULT = 100

    def __init__(self, pin_en, pin_in1, pin_in2):
        self._en = pin_en
        self._in1 = pin_in1
        self._in2 = pin_in2
        self._velocidad = Motor.LOW

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._in1,GPIO.OUT)
        GPIO.setup(self._in2,GPIO.OUT)
        GPIO.setup(self._en,GPIO.OUT)

        GPIO.output(self._in1,GPIO.LOW)
        GPIO.output(self._in2,GPIO.LOW)
        self.potencia = GPIO.PWM(self._en,100)
        self.potencia.start(self._velocidad)
    
    def __del__(self):
        print("Liberamos recursos")
        GPIO.cleanup()


    def avanzar(self):
        GPIO.output(self._in1,GPIO.HIGH)
        GPIO.output(self._in2,GPIO.LOW)

    def retroceder(self):
        GPIO.output(self._in1,GPIO.LOW)
        GPIO.output(self._in2,GPIO.HIGH)

    def stop(self):
        GPIO.output(self._in1,GPIO.LOW)
        GPIO.output(self._in2,GPIO.LOW)
        self._velocidad = Motor.LOW

    def velocidad_baja(self):
        self._velocidad = Motor.LOW
        self.potencia.ChangeDutyCycle(self._velocidad)

    def velocidad_media(self):
        self._velocidad = Motor.MID
        self.potencia.ChangeDutyCycle(self._velocidad)

    def velocidad_alta(self):
        self._velocidad = Motor.HIG
        self.potencia.ChangeDutyCycle(self._velocidad)
    
    def velocidad_top(self):
        self._velocidad = Motor.ULT
        self.potencia.ChangeDutyCycle(self._velocidad)
    




    

