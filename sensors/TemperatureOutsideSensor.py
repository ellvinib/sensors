from .ThingsBoardSensor import ThingsBoardSensor

from smbus2 import SMBus
from bmp280 import BMP280

class TemperatureOutsideSensor(ThingsBoardSensor):
    bmp280 = None
    def __init__(self):
        super().__init__('temperature')
        try:
            self.bmp280 = BMP280(i2c_dev=SMBus(1))
        except:
            print('Could not find temperature sensor')

    def getRawSensorValue(self):
        return self.bmp280.get_temperature()