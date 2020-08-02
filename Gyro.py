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
    # Scale Modifiers
    ACCEL_SCALE_MODIFIER_2G = 16384.0
    ACCEL_SCALE_MODIFIER_4G = 8192.0
    ACCEL_SCALE_MODIFIER_8G = 4096.0
    ACCEL_SCALE_MODIFIER_16G = 2048.0
    # Pre-defined ranges
    ACCEL_RANGE_2G = 0x00
    ACCEL_RANGE_4G = 0x08
    ACCEL_RANGE_8G = 0x10
    ACCEL_RANGE_16G = 0x18

    def __init__(self, address, bus=1):
        self.bus = smbus.SMBus(bus)
        # Wake up
        self.bus.write_byte_data(self.address, self.PWR_MGMT_1, 0x00)
    
    def read_accel_range(self, raw = False):
        raw_data = self.bus.read_byte_data(self.address, self.ACCEL_CONFIG)

        if raw is True:
            return raw_data
        elif raw is False:
            if raw_data == self.ACCEL_RANGE_2G:
                return 2
            elif raw_data == self.ACCEL_RANGE_4G:
                return 4
            elif raw_data == self.ACCEL_RANGE_8G:
                return 8
            elif raw_data == self.ACCEL_RANGE_16G:
                return 16
            else:
                return -1

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
        accel_scale_modifier = None
        accel_range = self.read_accel_range(True)

        if accel_range == self.ACCEL_RANGE_2G:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_2G
        elif accel_range == self.ACCEL_RANGE_4G:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_4G
        elif accel_range == self.ACCEL_RANGE_8G:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_8G
        elif accel_range == self.ACCEL_RANGE_16G:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_16G
        else:
            print("Unknown range-accel_scale_modifier set to self.ACCEL_SCALE_MODIFIER_2G")
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_2G

        x = self.read_i2c_word(self.ACCEL_XOUT0) * 9.81
        y = self.read_i2c_word(self.ACCEL_YOUT0) * 9.81
        z = self.read_i2c_word(self.ACCEL_ZOUT0) * 9.81

        x = x / accel_scale_modifier
        y = y / accel_scale_modifier
        z = z / accel_scale_modifier

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