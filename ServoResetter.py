from gpiozero import AngularServo
import time

print("Initialising Servos...")

servo1 = AngularServo(4, min_angle=-45, max_angle=45)
servo2 = AngularServo(17, min_angle=-45, max_angle=45)
servo3 = AngularServo(18, min_angle=-45, max_angle=45)
servo4 = AngularServo(27, min_angle=-45, max_angle=45)
servo5 = AngularServo(22, min_angle=-45, max_angle=45)
servo6 = AngularServo(23, min_angle=-45, max_angle=45)
servo7 = AngularServo(24, min_angle=-45, max_angle=45)
servo8 = AngularServo(25, min_angle=-45, max_angle=45)

servos = [servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8]

while True:
    i = input("Type Servo index to Test it: ")
    i = int(i) - 1
    servos[i].min()
    time.sleep(1)
    servos[i].mid()
    time.sleep(1)
    servos[i].max()
    time.sleep(1)
    servos[i].min()
