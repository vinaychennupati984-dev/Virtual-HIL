import socket
import pytest
import time
import subprocess
import sys
import os

HOST = "127.0.0.1"
PORT = 5001


def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall(command.encode())
        response = client.recv(1024).decode()
        return response


def wait_for_socket_server(timeout=15):
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as test_client:
                test_client.connect((HOST, PORT))
                return True
        except ConnectionRefusedError:
            time.sleep(0.5)

    return False


@pytest.fixture(scope="module", autouse=True)
def start_system():
    project_root = os.getcwd()

    process = subprocess.Popen(
        [sys.executable, "system_runner.py"],
        cwd=project_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    server_started = wait_for_socket_server(timeout=25)

    if not server_started:
        process.terminate()
        stdout, stderr = process.communicate(timeout=5)

        print("STDOUT:", stdout)
        print("STDERR:", stderr)

        pytest.fail("Socket server did not start on port 5001")

    yield

    process.terminate()
    process.wait()


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