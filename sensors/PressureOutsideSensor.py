from ThingsBoardSensor import ThingsBoardSensor

from smbus2 import SMBus
from bmp280 import BMP280

class PressureOutsideSensor(ThingsBoardSensor):
    bmp280;

    def __init__(self):
        super().__init__('pressure');
        try:
            self.bmp280 = BMP280(i2c_dev=SMBus(1))
        except:
            print('Could not find pressure sensor');

    def getRawSensorValue(self):
        return self.bmp280.get_pressure();