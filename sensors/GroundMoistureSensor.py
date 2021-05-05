from .ThingsBoardSensor import ThingsBoardSensor

import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class GroundMoistureSensor(ThingsBoardSensor):
    i2c = None
    ads2 = None
    chan = None

    def __init__(self):
        super().__init__('ground_moisture')
        try:
            self.i2c = busio.I2C(board.SCL, board.SDA)
            self.ads2 = ADS.ADS1115(self.i2c)
            self.chan = AnalogIn(self.ads2, ADS.P0)
        except Exception as e:
            print('Could not find the ground moisture sensor %s', e)

    def getRawSensorValue(self):
        return self.chan.value