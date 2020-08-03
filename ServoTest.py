from Gyro import Gyroscope
import time
from gpiozero import AngularServo

gy = Gyroscope(0x68)
servo0 = AngularServo(4, min_angle=-90, max_angle=90)

print("Starting Gyro Hookup")
while True:
    try:
        gyro_data = gy.get_gyro_data()
        servo0.angle = max(-90, min(gyro_data["x"], 90))

    except KeyboardInterrupt:
        break

    