class ThingsBoardSensor:
    name: str;
    
    def __init__(self, sensor_name):
        self.name = sensor_name
    
    def getSensorName(self):
        return self.name;

    def getRawSensorValue(self):
        return "error"

    def getSensorValue(self):
        try:
            return self.getRawSensorValue();
        except:
            return "error"