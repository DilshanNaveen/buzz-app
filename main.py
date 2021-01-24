from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socket = SocketIO(app)
socket.init_app(app, cors_allwed_origins="*")


@app.route('/')
def index():
    return render_template('index.html')


@socket.event
def send_message(data):
    socket.emit('receive_message', data)



if __name__ == '__main__':
    socket.run(app)
