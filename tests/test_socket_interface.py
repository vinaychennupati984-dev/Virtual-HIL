import socket
import pytest
import time

HOST = "127.0.0.1"
PORT = 5001


def send_command(command):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    client.sendall(command.encode())
    response = client.recv(1024).decode()

    client.close()
    return response


@pytest.fixture(scope="module", autouse=True)
def start_system():
    """
    Make sure your system_runner is running before tests.
    You can also automate this later.
    """
    print("\n[TEST] Ensure system_runner is running...")
    time.sleep(2)
    yield


def test_ecu1_set_speed():
    response = send_command("ECU1:SET_SPEED:50")
    assert "ACK" in response


def test_ecu1_get_status():
    send_command("ECU1:SET_SPEED:70")
    response = send_command("ECU1:GET_STATUS")

    assert "70" in response


def test_ecu2_process_speed():
    response = send_command("ECU2:PROCESS_SPEED:90")
    assert "ACK" in response


def test_invalid_command():
    response = send_command("INVALID")
    assert "ERROR" in response