from threading import Thread
from app.api import app, ecu2
from can_layer.can_listener import CANListener
import time

def run_api():
    app.run(host="0.0.0.0", port=5000)

def run_can():
    listener = CANListener(ecu2)
    while True:
        listener.listen()
        time.sleep(0.1)

if __name__ == "__main__":
    Thread(target=run_api).start()
    Thread(target=run_can).start()