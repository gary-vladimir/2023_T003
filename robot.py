import cyberpi
from time import sleep

class Robot:
    def __init__(self):
        self.ultraUp = 1
        self.ultraDown = 2
        self.clawDC = "m2"
        self.elevatorDC = "m1"
        self.lineFollower = 1
        self.colorSensor = 2
        self.clasifierServo = "s1"
        self.compartmentServo = "s2"
    
    def startRobot(self):
        cyberpi.ultrasonic2.led_show([80,80,80,80,80,80,80,80], index=self.ultraUp)
        cyberpi.ultrasonic2.led_show([80,80,80,80,80,80,80,80], index=self.ultraDown)
        self.compartment(90)
        self.classifier(90)          
    
    def closeClaw(self):
        cyberpi.mbot2.motor_set(100, self.clawDC)
        sleep(0.8)
        cyberpi.mbot2.motor_set(0, self.clawDC)

    def openClaw(self):
        cyberpi.mbot2.motor_set(-100, self.clawDC)
        sleep(0.8)
        cyberpi.mbot2.motor_set(0, self.clawDC)

    def elevateClaw(self):
        cyberpi.mbot2.motor_set(100, self.elevatorDC)
        sleep(0.8)
        cyberpi.mbot2.motor_set(0, self.elevatorDC)

    def compartment(self, angle):
        cyberpi.mbot2.servo_set(angle, self.compartmentServo)
        sleep(0.6)

    def classifier(self, angle):
        cyberpi.mbot2.servo_set(angle, self.clasifierServo)
        sleep(0.6)

    def move(left, right):
        cyberpi.mbot2.drive_power(left*-1, right)

    def stop():
        cyberpi.mbot2.EM_stop()

    def lineFollowerRead(self):
        lineStatus = cyberpi.quad_rgb_sensor.get_line_sta(index=self.lineFollower)
        return lineStatus
    