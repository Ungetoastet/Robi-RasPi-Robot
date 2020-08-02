import smbus
import math

class Gyroscope:
    # Global Vars
    address = 0x68
    bus = None
    # MPU-6050 Registers
    PWR_MGMT_1 = 0x6B
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
    
    def get_acceleration(self):
        x = self.read_i2c_word(self.ACCEL_XOUT0)
        y = self.read_i2c_word(self.ACCEL_YOUT0)
        z = self.read_i2c_word(self.ACCEL_ZOUT0)

        return {'x': x, 'y': y, 'z': z}

    def get_rotation(self):
        x = math.atan(self.get_acceleration()["y"] / self.get_acceleration()["z"]) * (180/math.pi)
        y = math.atan(self.get_acceleration()["z"] / self.get_acceleration()["x"]) * (180/math.pi)
        z = math.atan(self.get_acceleration()["x"] / self.get_acceleration()["y"]) * (180/math.pi)

        return {"x": x, "y": y, "z": z}