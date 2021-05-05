from Thingsboard import ThingsBoard
from sensors.LightSensor import LightSensor
from sensors.PressureOutsideSensor import PressureOutsideSensor
from sensors.SoilTemperatureSensor import SoilTemperatureSensor
from sensors.GroundMoistureSensor import GroundMoistureSensor
from sensors.TemperatureOutsideSensor import TemperatureOutsideSensor

import sys, time

# define connection to the sensor of our thingsboard

thingsBoard = ThingsBoard(sys.argv[1], sys.argv[2])

# Sensors we want to use in the things board

groundMoistureSensor = GroundMoistureSensor()
lightSensor = LightSensor()
pressureSensor = PressureOutsideSensor()
soilTemperatureSensor = SoilTemperatureSensor()
temperatureOutsideSensor = TemperatureOutsideSensor()

interval = 1

try:
    while True:
        thingsBoard.sendValuesToThingsBoard([groundMoistureSensor, lightSensor, pressureSensor, soilTemperatureSensor, temperatureOutsideSensor]);
        time.sleep(interval)
except KeyboardInterrupt:
    pass