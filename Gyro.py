#Modified version, original: https://github.com/Robocraze/MPU6050/blob/master/mpu6050.py
import smbus
import time
import math

class Gyroscope:

    # Global Vars
    address = 0x68
    bus = None
    ACCEL_CONFIG = 0x1C
    # MPU-6050 Registers
    PWR_MGMT_1 = 0x6B
    PWR_MGMT_2 = 0x6C
    ACCEL_XOUT0 = 0x3B
    ACCEL_YOUT0 = 0x3D
    ACCEL_ZOUT0 = 0x3F
    def __init__(self, address, bus=1):
        self.bus = smbus.SMBus(bus)
        # Wake up
        self.bus.write_byte_data(self.address, self.PWR_MGMT_1, 0x00)
    
    def read_i2c_word(self, register):
        # Read data
        high = self.bus.read_byte_data(self.address, register)
        low = self.bus.read_byte_data(self.address, register + 1)
        value = (high << 8) + low
        if (value >= 0x8000):
            return -((65535 - value) + 1)
        else:
            return value
    
    def get_accel_data(self):
        x = self.read_i2c_word(self.ACCEL_XOUT0)
        y = self.read_i2c_word(self.ACCEL_YOUT0)
        z = self.read_i2c_word(self.ACCEL_ZOUT0)
        return {'x': x, 'y': y, 'z': z}

    def get_gyro_data(self):
        x = math.atan(self.get_accel_data()["y"] / self.get_accel_data()["z"]) * (180/math.pi)
        y = math.atan(self.get_accel_data()["z"] / self.get_accel_data()["x"]) * (180/math.pi)
        z = math.atan(self.get_accel_data()["x"] / self.get_accel_data()["y"]) * (180/math.pi)
        return {"x": x, "y": y, "z": z}

mpu = Gyroscope(0x68)

if __name__ == "__main__":
    while True:
        try:
           accel_data = mpu.get_accel_data()
           gyro_data = mpu.get_gyro_data()

           print("Ax:{:.4f}\tAy:{:.4f}\tAz:{:.4f}\tGx:{:.4f}\tGy:{:.4f}\tGz:{:.4f} ".format(accel_data['x'], accel_data['y'], accel_data['z'], gyro_data['x'], gyro_data['y'], gyro_data['z']))

        except KeyboardInterrupt:
            break

        time.sleep(1)