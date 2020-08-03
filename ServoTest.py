from Gyro import Gyroscope
import time
from gpiozero import AngularServo

gy = Gyroscope(0x68)
servo0 = AngularServo(4, min_angle=-45, max_angle=45)

print("Starting Gyro Hookup")
while True:
    try:
        gyro_data = gy.get_gyro_data()
        angle1 = max(45, min(gyro_data["x"], -45))
        servo0.angle = angle1

    except KeyboardInterrupt:
        break