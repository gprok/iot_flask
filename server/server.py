from flask import Flask, request, jsonify, render_template 
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('data.db')

print "Opened database successfully";

# Create tables if they do not exist
conn.execute('''CREATE TABLE IF NOT EXISTS sensors
         (ID INT PRIMARY KEY     NOT NULL,
          SENSOR_ID      INT     NOT NULL,
          TYPE           TEXT    NOT NULL,
          LON            REAL     NOT NULL,
          LAT            REAL     NOT NULL,
          VALUE          REAL     NOT NULL,
          VALUE_DT       TEXT     NOT NULL);''')

@app.route("/")
def home():
    return "<h1>IoT Flask Server</h1>"

@app.route("/api/send", methods=['POST'])
def api_send():
    post_data = request.json
    print(post_data)
    return jsonify({'result': 'data received'})

@app.route("/data")
def data():
    # Get all sensor data from the database
    # Create html page to display data and pass data to the page
    return render_template('data.html')
