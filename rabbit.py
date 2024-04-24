import paho.mqtt.client as mqtt
import json
import logging
from pymongo import MongoClient

logging.basicConfig(level=logging.INFO)

db_connect = MongoClient('mongodb://localhost:27017/')
db = db_connect['iot_data']
collection = db['mqtt_messages']

def insert_mqtt_message(topic, data):
    try:
        collection.insert_one({
            "topic": topic,
            "message": {
                "sensor_id": data["sensor_id"],
                "timestamp": data["timestamp"],
                "data": {
                    "type": data["data"]["type"],
                    "value": data["data"]["value"],
                    "unit": data["data"]["unit"]
                }
            }
        })
        logging.info("Inserted message into MongoDB: %s", data)
    except Exception as e:
        logging.error("Error inserting message into MongoDB: %s", str(e))

def process_message(data):
    if "sensor_id" in data:
        sensor_id = data["sensor_id"]
        if sensor_id == "123":
            if "value" in data["data"] and data["data"]["unit"] == "Celsius":
                celsius = data["data"]["value"]
                fahrenheit = celsius * 1.8 + 32
                data["data"]["value"] = fahrenheit
                data["data"]["unit"] = "Fahrenheit"
    return data

def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())
        processed_data = process_message(data)
        insert_mqtt_message(message.topic, processed_data)
    except Exception as e:
        logging.error("Error processing message: %s", str(e))

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe("iot_testdata")

client.loop_forever()
