import socket
import time


HOST = "127.0.0.1"
PORT = 5001


def send_command(command: str) -> str:
    
    retries = 3

    for attempt in range(retries):

        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # client timeout
            client.settimeout(5)

            client.connect((HOST, PORT))

            client.sendall(command.encode("utf-8"))

            response = client.recv(1024).decode("utf-8")

            client.close()

            return response

        except (socket.timeout, ConnectionRefusedError) as error:

            print(f"[CLIENT] Retry {attempt + 1}/{retries} due to: {error}")

            time.sleep(1)

    return "ERROR:SERVER_UNAVAILABLE"


if __name__ == "__main__":
    commands = [
        "ECU1:SET_SPEED:60",
        "ECU1:GET_STATUS",
        "ECU2:PROCESS_SPEED:90",
        "ECU2:GET_STATUS"
    ]

    for command in commands:
        print(f"{command} -> {send_command(command)}")