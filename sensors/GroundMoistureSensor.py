from ThingsBoardSensor import ThingsBoardSensor

import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class GroundMoistureSensor(ThingsBoardSensor):
    i2c;
    ads2;
    chan;

    def __init__(self):
        super().__init__('ground_moisture');
        try:
            self.i2c = busio.I2C(board.SCL, board.SDA);
            self.ads2 = ADS.ADS1115(i2c);
            self.chan = AnalogIn(ads2, ADS.P0);
        except:
            print('Could not find the ground moisture sensor');

    def getRawSensorValue(self):
        return self.chan.value;