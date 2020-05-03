from motor import Motor

class Tanque:

    def __init__(self, en_l, in1_l, in2_l, en_r, in1_r, in2_r):
        self._motor_l = Motor(en_l, in1_l, in2_l)
        self._motor_r = Motor(en_r, in1_r, in2_r)

    def avanzar(self):
        self._motor_l.avanzar()
        self._motor_r.avanzar()

    def retroceder(self):
        self._motor_l.retroceder()
        self._motor_r.retroceder()

    def stop(self):
        self._motor_l.stop()
        self._motor_r.stop()

    def giro_izq_1(self):
        self._motor_l.stop()
        self._motor_r.avanzar()

    def giro_izq_2(self):
        self._motor_l.retroceder()
        self._motor_r.avanzar()

    def giro_der_1(self):
        self._motor_r.stop()
        self._motor_l.avanzar()

    def giro_der_2(self):
        self._motor_r.retroceder()
        self._motor_l.avanzar()

    def velocidad_alta(self):
        self._motor_l.velocidad_alta()
        self._motor_r.velocidad_alta()
    
    def velocidad_media(self):
        self._motor_l.velocidad_media()
        self._motor_r.velocidad_media()

    def velocidad_baja(self):
        self._motor_l.velocidad_baja()
        self._motor_r.velocidad_baja()

        