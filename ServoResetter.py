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

print("Beginning reset")

i = 0
for x in servos:
    servos[i].mid()
    time.sleep(0.5)
    print("Resetted servo " + str(i))
    i += 1

print("Reset done!")
