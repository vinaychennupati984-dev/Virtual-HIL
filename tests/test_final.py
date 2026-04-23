import time
from app.ecu1_service import ECU1Service
from app.ecu2_service import ECU2Service
from can_layer.can_listener import CANListener

def test_system_flow():
    ecu1 = ECU1Service()
    ecu2 = ECU2Service()
    listener = CANListener(ecu2)

    ecu1.set_speed(90)

    for _ in range(5):
        listener.listen()
        time.sleep(0.1)

    state = ecu2.get_status()

    assert state["speed"] == 90
    assert state["brake"] is True