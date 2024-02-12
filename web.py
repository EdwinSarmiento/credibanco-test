from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    current_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    return f'Hola Edwin, la fecha y hora actual es: {current_time}'

if __name__ == '__main__':
    app.run(debug=True)