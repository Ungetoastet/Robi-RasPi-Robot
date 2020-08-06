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
    command = input()
    if command == "help":
        print("standby: Lay down")
        print("idle: Stand up")

    if command == "idle":
        servos[0].mid()
        servos[1].mid()
        servos[2].mid()
        servos[3].mid()
        servos[4].min()
        servos[5].max()
        servos[6].min()
        servos[7].max()
        time.sleep(1)
    
    if command == "standby":
        servos[0].mid()
        servos[1].mid()
        servos[2].mid()
        servos[3].mid()
        servos[4].max()
        servos[5].min()
        servos[6].max()
        servos[7].min()
        time.sleep(1)