#https://www.engineersgarage.com/raspberrypi/articles-raspberry-pi-i2c-bus-pins-smbus-smbus2-python/

import json
import requests
import time
from bmp280 import BMP280
from BH1750 import BH1750
from w1thermsensor import W1ThermSensor

#
import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

# generic bus data
bus = SMBus(1)
# sepecific i2C BMP280 sensor data
bmp280 = BMP280(i2c_dev=bus)
# sepecific i2C BH1750 sensor data
gy30 = BH1750(bus)
# DS18B20 1 wire sensor
ds18b20 = W1ThermSensor()
# ADS115 i2C sensor
i2c = busio.I2C(board.SCL, board.SDA)
ads2 = ADS.ADS1115(i2c)
chan = AnalogIn(ads2, ADS.P0)

THINGSBOARD_HOST = '193.191.187.65'
ACCESS_TOKEN = 'Sensors1'
url = "http://"+THINGSBOARD_HOST+":80/api/v1/"+ACCESS_TOKEN+"/telemetry"

sensor_data = {'temperature':0, 'pressure': 0, 'light_intensity': 0, 'ground_temperature': 0, 'ground_moisture': 0}

interval = 1

#TODO: catch failure of sensors

try:
    while True:
        #BMP280 sensor data
        sensor_data['temperature'] = bmp280.get_temperature()
        sensor_data['pressure'] = bmp280.get_pressure()
        sensor_data['light_intensity'] = gy30.measure_low_res()
        sensor_data['ground_temperature'] = ds18b20.get_temperature()
        sensor_data['ground_moisture'] = chan.value

        response = requests.post(url, json=sensor_data)
        #print values
        print('{:0}:::: {:05.2f}*C {:05.2f}hPa {:05.2f}lx {:05.2f}G*C {:05.2f}GMD'.format(response.status_code, sensor_data['temperature'], sensor_data['pressure'], sensor_data['light_intensity'], sensor_data['ground_temperature'], sensor_data['ground_moisture']))

        time.sleep(interval)
except KeyboardInterrupt:
    pass