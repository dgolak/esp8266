import machine
import time


class engines:
    """Motor engine L298N connected to ESP8266 compatible with micropython."""
    def __init__(self, machine):
        self.machine = machine
        self.left_first_pin = 0
        self.left_second_pin = 5
        self.right_first_pin = 12
        self.right_second_pin = 14

    def forward(self, duty=1000):
        """All engines run go to forward."""
        self.stop()
        e1=machine.PWM(self.machine.Pin(self.left_first_pin),freq=100,duty=duty)
        e2=machine.PWM(self.machine.Pin(self.right_second_pin),freq=100,duty=duty)


    def back(self, duty=1000):
        """All engines run go to backward."""
        self.stop()
        e1=machine.PWM(self.machine.Pin(self.left_second_pin),freq=100,duty=duty)
        e2=machine.PWM(self.machine.Pin(self.right_first_pin),freq=100,duty=duty)


    def left(self):
        """Left engine speed 100 and right engine speed 400."""
        self.stop()
        e1=machine.PWM(self.machine.Pin(self.left_first_pin), freq=100, duty=1000)
        e2=machine.PWM(machine.Pin(self.right_first_pin), freq=100, duty=400)

    def right(self):
        """Right engine speed 100 and left engine speed 400."""
        self.stop()
        e1=machine.PWM(self.machine.Pin(self.left_second_pin),freq=100,duty=400)
        e2=machine.PWM(self.machine.Pin(self.right_second_pin),freq=100,duty=1000)

    def stop(self):
        """Engines stop."""
        machine.PWM(self.machine.Pin(self.left_first_pin),freq=0,duty=0)
        machine.PWM(self.machine.Pin(self.right_second_pin),freq=0,duty=0)
        machine.PWM(self.machine.Pin(self.left_second_pin),freq=0,duty=0)
        machine.PWM(self.machine.Pin(self.right_first_pin),freq=0,duty=0)

E=engines(machine)
