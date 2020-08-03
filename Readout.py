from Gyro import Gyroscope
import time

gy = Gyroscope(0x68)
print("Starting Readout")
while True:
    try:
        accel_data = gy.get_accel_data()
        gyro_data = gy.get_gyro_data()

        print("Ax:{:.4f}\tAy:{:.4f}\tAz:{:.4f}\tGx:{:.4f}\tGy:{:.4f}\tGz:{:.4f} ".format(accel_data['x'], accel_data['y'], accel_data['z'], gyro_data['x'], gyro_data['y'], gyro_data['z']))

    except KeyboardInterrupt:
        break

    time.sleep(1)