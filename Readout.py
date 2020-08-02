from Gyro import Gyroscope
import time

print("Starting Readout")
while True:
    print("Ax:{:.4f}\tAy:{:.4f}\tAz:{:.4f}\tGx:{:.4f}\tGy:{:.4f}\tGz:{:.4f} ".format(Gyroscope.get_accel_data(Gyroscope)['x'], Gyroscope.get_accel_data(Gyroscope)['y'], Gyroscope.get_accel_data(Gyroscope)['z'], Gyroscope.get_gyro_data(Gyroscope)['x'], Gyroscope.get_gyro_data(Gyroscope)['y'], Gyroscope.get_gyro_data(Gyroscope)['z']))
    time.sleep(1)