import requests 
import random
import time
import json

class Server:
    url = 'http://127.0.0.1:5000/api/send'
    


class HumiditySensor:
    def __init__(self, id, lon, lat):
        self.type = "humidity"
        self.id = id 
        self.lon = lon 
        self.lat = lat 
        
    def send_data(self):
        r = random.uniform(60.0, 100.0)
        data = {
            "id": self.id, 
            "type": self.type,  
            "lon": self.lon,  
            "lat": self.lat,
            "data": {"humidity": r}
        }
        print("sending data ...", Server.url)
        response = requests.post(Server.url, json=data)
        print(response.status_code, response.reason)
        
        

s = HumiditySensor(1, 23.456, 45.190)
for i in range(10):
    s.send_data()
    time.sleep(3)
    
        
        
        
        
        
        
    