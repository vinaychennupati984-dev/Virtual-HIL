import socket


HOST = "127.0.0.1"
PORT = 5001


def send_command(command: str) -> str:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    client.sendall(command.encode("utf-8"))
    response = client.recv(1024).decode("utf-8")

    client.close()
    return response


if __name__ == "__main__":
    commands = [
        "ECU1:SET_SPEED:60",
        "ECU1:GET_STATUS",
        "ECU2:PROCESS_SPEED:90",
        "ECU2:GET_STATUS"
    ]

    for command in commands:
        print(f"{command} -> {send_command(command)}")