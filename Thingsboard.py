import json
import requests

class ThingsBoard:
    thingsboard_host: str
    thingsboard_client_access_token: str
    thingsboard_url: str
    
    def __init__(self, thingsboard_host, thingsboard_client_access_token):
        self.thingsboard_host = thingsboard_host;
        self.thingsboard_client_access_token = thingsboard_client_access_token;
        
    def getThingsboardUrl(self):
        return "http://"+self.thingsboard_host+":80/api/v1/"+self.thingsboard_client_access_token+"/telemetry";
    
    def createJsonObject(self, data:List[ThingsBoardSensor]):
        data = {};
        for i in data:
            data[i.getSensorName()] = i.getSensorValue();
        return json.dumps(data);
    
    def sendValuesToThingsBoard(self, values: List[ThingsBoardSensor]):
        jsonData = self.createJsonObject(values);
        print(jsonData);
        return requests.post(self.getThingsboardUrl(), json=jsonData);