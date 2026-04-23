import requests
import time

BASE_URL = "http://127.0.0.1:5000"

def set_speed(speed):
    print(f"\n[CLIENT] Sending speed: {speed}")
    res = requests.post(f"{BASE_URL}/set_speed", json={"speed": speed})
    print("[CLIENT] Response:", res.json())

def get_ecu2_status():
    res = requests.get(f"{BASE_URL}/ecu2")
    print("[CLIENT] ECU2 State:", res.json())

if __name__ == "__main__":
    # send speed
    for speed in [40, 70, 90, 60]:
        set_speed(speed)
    time.sleep(1)
    get_ecu2_status()