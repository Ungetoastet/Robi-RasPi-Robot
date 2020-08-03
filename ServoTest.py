from Gyro import Gyroscope
import time
from gpiozero import AngularServo

gy = Gyroscope(0x68)
servoX = AngularServo(4, min_angle=-45, max_angle=45)

print("Starting Gyro Hookup")
while True:
    try:
        gyro_data = gy.get_gyro_data()
        servoX.angle = max(-45, min(gyro_data["x"], 45))

    except KeyboardInterrupt:
        servoX.mid()
        print("Servo Test Stopped")
        break

    