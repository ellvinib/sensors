import json
import requests
from typing import List
from sensors.ThingsBoardSensor import ThingsBoardSensor

class ThingsBoard:
    thingsboard_host = None
    thingsboard_client_access_token = None
    thingsboard_url = None
    
    def __init__(self, thingsboard_host, thingsboard_client_access_token):
        self.thingsboard_host = thingsboard_host
        self.thingsboard_client_access_token = thingsboard_client_access_token
        
    def getThingsboardUrl(self):
        return "http://"+self.thingsboard_host+":80/api/v1/"+self.thingsboard_client_access_token+"/telemetry"
    
    def createJsonObject(self, data:List[ThingsBoardSensor]):
        dataObj = {}
        for i in data:
            dataObj[i.getSensorName()] = i.getSensorValue()
        return dataObj
    
    def sendValuesToThingsBoard(self, values: List[ThingsBoardSensor]):
        jsonData = self.createJsonObject(values)
        request = requests.post(self.getThingsboardUrl(), json=jsonData)
        if (request.status_code == 200):
            print ('values send to thingsboard: ', jsonData)
        else:
            print('Connection error while sending values to thingsboard code %s', request.status_code, jsonData)
        return request