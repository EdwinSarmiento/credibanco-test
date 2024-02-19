from flask import Flask
from flask_testing import TestCase
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    current_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    return f'Hola Edwin, la fecha y hora actual es: {current_time}'

class MyTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hola Edwin", response.data.decode('utf-8'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)