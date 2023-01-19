from flask import Flask, request, jsonify, render_template 
import sqlite3
import random 

app = Flask(__name__)

conn = sqlite3.connect('data.db')

print("Opened database successfully");

# Create tables if they do not exist
conn.execute('''CREATE TABLE IF NOT EXISTS sensors
         (ID INTEGER  PRIMARY KEY  AUTOINCREMENT,
          SENSOR_ID      INTEGER     NOT NULL,
          TYPE           TEXT    NOT NULL,
          LON            REAL     NOT NULL,
          LAT            REAL     NOT NULL,
          VALUE          REAL     NOT NULL,
          VALUE_DT       TEXT     NOT NULL);''')

# Populate DB with sample data, if table is empty
cursor = conn.cursor()
cursor.execute("SELECT * FROM sensors")
rows = cursor.fetchall()
print("ROWS ", len(rows))
if len(rows) == 0:
    fake_sensors = {
        1: ['humidity', 34.127876, 24.890762], 
        2: ['temperature', 34.127876, 24.890762],
        3: ['light', 34.127876, 24.890762]
    }
    insert_sql = "INSERT INTO sensors (sensor_id, type, lon, lat, value, value_dt) VALUES (?,?,?,?,?,?)"
    for i in range(1, 11):
        rnd = random.randint(1, 3)
        sensor = fake_sensors[rnd]
        cursor.execute(insert_sql, (rnd, sensor[0], sensor[1], sensor[2], random.randint(1, 100), "2023-01-19 18:10:10"))
    conn.commit()


@app.route("/")
def home():
    return "<h1>IoT Flask Server</h1>"

@app.route("/api/send", methods=['POST'])
def api_send():
    post_data = request.json
    print(post_data)
    # create cursor and run insert just like line 32 and 36
    return jsonify({'result': 'data received'})

@app.route("/data")
def data():
    # Get all sensor data from the database
    # Create html page to display data and pass data to the page
    return render_template('data.html')
