from django.test import TestCase, Client

class GeneratorViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_single_sensor_actuator(self):
        data = {
            'ssid': 'TestNet',
            'password': 'TestPass',
            'sensor_type': ['DHT11'],
            'sensor_pin': ['Pin1'],
            'interval': ['5'],
            'act_type': ['RelayLight'],
            'act_pin': ['Pin2'],
            'trigger': ['motion_detected'],
        }
        response = self.client.post('/', data)
        self.assertEqual(response.status_code, 200)
        content = response.content.decode()
        # Check for key lines
        self.assertIn('wifi.connect("TestNet", "TestPass")', content)
        self.assertIn('# DHT11 on Pin1, interval=5s', content)
        self.assertIn('# RelayLight on Pin2, trigger=motion_detected', content)
