from Gyro import Gyroscope
import time
from gpiozero import AngularServo

gy = Gyroscope(0x68)
servo0 = AngularServo(4, min_angle=-45, max_angle=45)

print("Starting Gyro Hookup")
while True:
    try:
        gyro_data = gy.get_gyro_data()
        servo0.angle = max(-45, min(gyro_data["x"], 45))
        time.sleep(0.25)

    except KeyboardInterrupt:
        break

    