import unittest
from unittest.mock import MagicMock
from rabbit import process_message, insert_mqtt_message

class TestProcessMessage(unittest.TestCase):
    def test_process_message_no_sensor_id(self):
        data = {"value": 25.5, "unit": "Celsius"}
        processed_data = process_message(data)
        self.assertEqual(data, processed_data, "Data should remain unchanged without sensor_id")

    def test_process_message_sensor_celsius(self):
        data = {"sensor_id": "123", "value": 25.5, "unit": "Celsius"}
        processed_data = process_message(data)
        expected_data = {"sensor_id": "123", "value": 77.9, "unit": "Fahrenheit"}  
        self.assertEqual(expected_data, processed_data, "Data should be converted to Fahrenheit")

    def test_process_message_sensor_fahrenheit(self):
        data = {"sensor_id": "123", "value": 77.9, "unit": "Fahrenheit"}
        processed_data = process_message(data)
        expected_data = {"sensor_id": "123", "value": 77.9, "unit": "Fahrenheit"}  
        self.assertEqual(expected_data, processed_data, "Data should remain unchanged in Fahrenheit")

class TestInsertMqttMessage(unittest.TestCase):
    def setUp(self):
        self.collection_mock = MagicMock()
        self.db_mock = MagicMock()
        self.db_mock['mqtt_messages'] = self.collection_mock

    def test_insert_mqtt_message(self):
        data = {
            "sensor_id": "456",
            "timestamp": "2024-04-23T12:01:00Z",
            "data": {
                "type": "humidity",
                "value": 60.0,
                "unit": "percentage"
            }
        }
        insert_mqtt_message("test_topic", data, self.db_mock)
        self.collection_mock.insert_one.assert_called_with({
            "topic": "test_topic",
            "message": data
        })

if __name__ == '__main__':
    unittest.main()
