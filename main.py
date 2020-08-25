from gpiozero import AngularServo
import time

print("Initialising Servos...")

gpio = [4, 17, 18, 27, 22, 23, 24, 25]
angleMult = [1, -1, 1, -1, 1, -1, 1, -1]
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
        print("pushups: Stand up and do pushups")
        print("shutdown: Lay down and quit")

    elif command == "standby":
        for x in range(3):
            servos[x].angle = 0
            servos[x + 4].angle = 45 * angleMult[x + 4] 
            
        time.sleep(1)

    elif command == "idle":
        for x in range(3):
            servos[x].angle = 25 * angleMult[x]
            servos[x + 4].angle = -45 * angleMult[x + 4]
        time.sleep(1)

    elif command == "pushups":
        active = True
        while active:
            try:
                for x in range(3):
                    servos[x].angle = 0
                    servos[x + 4].angle = -45 * angleMult[x + 4]
                time.sleep(1)
                for x in range(3):
                    servos[x].angle = -45 * angleMult[x]
                    servos[x + 4].angle = 0
                time.sleep(0.5)
            except KeyboardInterrupt:
                active = False

    elif command == "shutdown":
        for x in range(3):
            servos[x].angle = 0
            servos[x + 4].angle = 45 * angleMult[4]
        time.sleep(1)
        quit()
    
    else:
        print("Command not found. Type 'help' for commands")