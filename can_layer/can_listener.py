from can_layer.can_interface import CANInterface
from can_layer.dbc_handler import DBCHandler

class CANListener:
    def __init__(self, ecu2_service):
        self.can = CANInterface()
        self.dbc = DBCHandler("dbc/vehicle.dbc")
        self.ecu2 = ecu2_service

    def listen(self):
        msg = self.can.receive()

        if msg:
            decoded = self.dbc.decode("VehicleSpeed", msg.data)
            speed = decoded["speed"]

            self.ecu2.process_speed(speed)
            print(f"[ECU2] Received speed={speed}, brake={self.ecu2.get_status()['brake']}")