from threading import Thread
import time

from app.api import app, ecu1, ecu2
from can_layer.can_listener import CANListener
from socket_layer.socket_server import run_socket_server


def run_api():
    app.run(host="0.0.0.0", port=5000)


def run_can():
    listener = CANListener(ecu2)

    while True:
        listener.listen()
        time.sleep(0.1)


if __name__ == "__main__":
    Thread(target=run_api, daemon=True).start()
    Thread(target=run_can, daemon=True).start()
    Thread(target=run_socket_server, args=(ecu1, ecu2), daemon=True).start()

    print("[SYSTEM] Virtual HIL running with REST API + CAN + TCP Socket")

    while True:
        time.sleep(1)