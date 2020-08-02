from Gyro import Gyroscope
import time

print("Starting Readout")
while True:
    print("Ax:{:.4f}\tAy:{:.4f}\tAz:{:.4f}\tGx:{:.4f}\tGy:{:.4f}\tGz:{:.4f} ".format(Gyroscope.get_acceleration(Gyroscope)['x'], Gyroscope.get_acceleration(Gyroscope)['y'], Gyroscope.get_acceleration(Gyroscope)['z'], Gyroscope.get_rotation(Gyroscope)['x'], Gyroscope.get_rotation(Gyroscope)['y'], Gyroscope.get_rotation(Gyroscope)['z']))
    time.sleep(1)