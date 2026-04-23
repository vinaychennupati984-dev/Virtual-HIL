from app.ecu1_core import ECU1Core
from can_layer.can_interface import CANInterface
from can_layer.dbc_handler import DBCHandler

class ECU1Service:
    def __init__(self):
        self.core = ECU1Core()
        self.can = CANInterface()
        self.dbc = DBCHandler("dbc/vehicle.dbc")

    def set_speed(self, speed):
        self.core.update_speed(speed)

        data = self.dbc.encode("VehicleSpeed", {"speed": speed})
        self.can.send(0x100, data)

    def get_status(self):
        return self.core.get_state()