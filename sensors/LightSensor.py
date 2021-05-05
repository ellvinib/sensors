from ThingsBoardSensor import ThingsBoardSensor

from smbus2 import SMBus
from BH1750 import BH1750

class LightSensor(ThingsBoardSensor):
    gy30;

    def __init__(self):
        super().__init__('light_intensity');
        try:
            self.gy30 = BH1750(SMBus(1));
        except:
            print('Could not find light intensity sensor');

    def getRawSensorValue(self):
        return self.gy30.measure_low_res();