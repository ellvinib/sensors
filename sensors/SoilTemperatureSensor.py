from ThingsBoardSensor import ThingsBoardSensor

from w1thermsensor import W1ThermSensor

class SoilTemperatureSensor(ThingsBoardSensor):
    ds18b20;

    def __init__(self):
        super().__init__('ground_temperature');
        try:
            self.ds18b20 = W1ThermSensor()
        except:
            print('Could not find soil temperature sensor');

    def getRawSensorValue(self):
        return self.ds18b20.get_temperature();