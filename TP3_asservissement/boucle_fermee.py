from time import time, sleep
from threading import Thread

from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B

motor = Motor(OUTPUT_A)

class PID(Thread):
    def __init__(self, motor: Motor, Kp=1, Ki=1, Kd=1):
        Thread.__init__(self)
        self.motor = motor
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.integral = 0
        self.last_error = 0
        self.error = 100
        self.dt = 0


    def run(self):
        self.running = True

        while self.running:
            self.integral += self.error * self.dt
            derivative = (self.error - self.last_error) / self.dt
            self.last_error = self.error
            output = self.Kp * self.error + self.Ki * self.integral + self.Kd * derivative
            self.motor.on(output)

            sleep(0.1)

    def stop(self):
        self.running = False
        self.motor.off()


# coefficients PID
KP = 1
KI = 1
KD = 1

esclave_1 = PID(motor, KP, KI, KD)
esclave_2 = PID(motor, KP, KI, KD)