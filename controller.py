from inputs import devices, get_gamepad 

LeftX = 0
LeftY = 0
RightX = 0
RightY = 0

print("Detected devices:")
for device in devices.gamepads:
    print(device)
print("Starting readout...")

while True:
    events = get_gamepad()
    for event in events:
        if event.code == "ABS_X":
            LeftX = int(event.state / 327)
        if event.code == "ABS_Y":
            LeftY = int(event.state / 327)
        if event.code == "ABS_RX":
            RightX = int(event.state / 327)
        if event.code == "ABS_RY":
            RightY = int(event.state / 327)
    print(str(LeftX) + " " + str(LeftY) + " " + str(RightX) + " " + str(RightY))