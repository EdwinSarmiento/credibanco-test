from flask_testing import TestCase
from flask import Flask
import web.py

class MyTest(TestCase):
    def create_app(self):
        app = your_flask_app_file.app
        app.config['TESTING'] = True
        return app

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hola Edwin", response.data.decode('utf-8'))