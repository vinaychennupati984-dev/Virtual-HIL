import can

class CANInterface:
    def __init__(self):
        self.bus = can.Bus(interface='virtual', channel='test', receive_own_messages=True)

    def send(self, msg_id, data):
        msg = can.Message(arbitration_id=msg_id, data=data, is_extended_id=False)
        self.bus.send(msg)

    def receive(self):
        return self.bus.recv(timeout=1)