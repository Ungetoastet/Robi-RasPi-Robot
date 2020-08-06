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

while True:
    servo1.max()
    servo2.min()
    servo3.max()
    servo4.min()
    servo5.min()
    servo6.max()
    servo7.min()
    servo8.max()
    time.sleep(1)