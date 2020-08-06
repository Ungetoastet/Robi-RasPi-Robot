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
    command = input(">>")
    if command == "help":
        print("standby: Lay down")
        print("idle: Stand up")
        print("wiggle: Stand up and shake")
        print("shutdown: Lay down and quit")

    elif command == "standby":
        servos[0].mid()
        servos[1].mid()
        servos[2].mid()
        servos[3].mid()
        servos[4].max()
        servos[5].min()
        servos[6].max()
        servos[7].min()
        time.sleep(1)

    elif command == "idle":
        servos[0].mid()
        servos[1].mid()
        servos[2].mid()
        servos[3].mid()
        servos[4].min()
        servos[5].max()
        servos[6].min()
        servos[7].max()
        time.sleep(1)

    elif command == "wiggle":
        servos[0].mid()
        servos[1].mid()
        servos[2].mid()
        servos[3].mid()
        servos[4].min()
        servos[5].max()
        servos[6].min()
        servos[7].max()
        active = True
        while active:
            try:
                servos[0].mid()
                servos[1].mid()
                servos[2].mid()
                servos[3].mid()
                time.sleep(1)
                servos[0].max()
                servos[1].min()
                servos[2].max()
                servos[3].min()
                time.sleep(1)
            except KeyboardInterrupt:
                active = False
                
    elif command == "shutdown":
        servos[0].mid()
        servos[1].mid()
        servos[2].mid()
        servos[3].mid()
        servos[4].max()
        servos[5].min()
        servos[6].max()
        servos[7].min()
        time.sleep(1)
        quit()
    
    else:
        print("Command not found. Type 'help' for commands")