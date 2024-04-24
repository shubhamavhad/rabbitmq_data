# rabbitmq_data
Process of the task:-
1.rabbit mq installation :-
process:-
step 1: Install RabbitMQ and Required Packages
step 2:-Enable Web Management Dashboard
step 3:-Install MQTT Plugin
step 4:-Configure MQTT Plugin
step 5:-Open Port for MQTT

2.code explanation :-
1.Required Libraries
paho.mqtt.client: Library for MQTT client functionality.
json: Library for working with JSON data.
logging: Library for logging messages.
pymongo: Library for interfacing with MongoDB.
2. MongoDB Configuration
Establishes a connection to the MongoDB server running on localhost:27017.
Uses the iot_data database and the mqtt_messages collection.
3. Function to Insert MQTT Messages into MongoDB
   Function Name: insert_mqtt_message(topic, data)
4.Function to Process MQTT Message
  Function Name: process_message(data)
5.MQTT on_message Callback Function
  Function Name: on_message(client, userdata, message)
6.MQTT Client Setup and Connection


refrences:-
https://pypi.org/project/paho-mqtt/
https://pypi.org/project/pymongo/
