from app.ecu2_core import ECU2Core

class ECU2Service:
    def __init__(self):
        self.core = ECU2Core()

    def process_speed(self, speed):
        self.core.update_speed(speed)

    def get_status(self):
        return self.core.get_state()