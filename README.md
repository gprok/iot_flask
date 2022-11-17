# Simple IoT with Python and Flask

**server**: code for the Flask server  

**sensors**: simulated arduino (not accurate) sensors 

## Instructions 

Clone project: ```git clone https://github.com/gprok/iot_flask.git```   
cd in iot_flask directory: ```cd iot_flask```    
Create virtual environment: ```python -m venv venv```   
activate it: (Mac/Linux) ```. venv/bin/activate```, (Win) ```venv\Scripts\activate```    
Install libraries: pip install -r requirements.txt```    

Start server: 
```cd server```   
```flask --app server run```   

Run sensors:
Open a new terminal in VS Code   
```cd sensors```    
activate venv in new terminal
```python sensors.py```   
