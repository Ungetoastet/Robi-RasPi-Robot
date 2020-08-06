from gpiozero import AngularServo
import time

print("Initialising Servos...")

gpio = [4, 17, 18, 27, 22, 23, 24, 25]
servos = []
iteration = 0
for x in gpio:
    servos.append(AngularServo(gpio[iteration],  min_angle=-45, max_angle=45))
    iteration += 1

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
