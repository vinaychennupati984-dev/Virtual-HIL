import socket
from threading import Thread

from app.ecu1_service import ECU1Service
from app.ecu2_service import ECU2Service


HOST = "127.0.0.1"
PORT = 5001


class SocketServer:
    """
    TCP socket interface for Virtual HIL.

    This simulates Ethernet-style command/response communication
    between a test client and virtual ECUs.
    """

    def __init__(self, ecu1_service=None, ecu2_service=None):
        self.ecu1 = ecu1_service if ecu1_service else ECU1Service()
        self.ecu2 = ecu2_service if ecu2_service else ECU2Service()

    def process_command(self, command: str) -> str:
        command = command.strip()

        try:
            if command.startswith("ECU1:SET_SPEED:"):
                speed = int(command.split(":")[2])
                self.ecu1.set_speed(speed)
                return f"ACK:ECU1:SPEED_SET:{speed}"

            if command == "ECU1:GET_STATUS":
                return str(self.ecu1.get_status())

            if command.startswith("ECU2:PROCESS_SPEED:"):
                speed = int(command.split(":")[2])
                self.ecu2.process_speed(speed)
                return f"ACK:ECU2:SPEED_PROCESSED:{speed}"

            if command == "ECU2:GET_STATUS":
                return str(self.ecu2.get_status())

            return "ERROR:UNKNOWN_COMMAND"

        except Exception as error:
            return f"ERROR:{error}"

    def handle_client(self, connection, address):
        print(f"[SOCKET] Client connected: {address}")

        # Added timeout handling
        connection.settimeout(5)

        try:
            while True:
                data = connection.recv(1024)

                if not data:
                    break

                command = data.decode("utf-8")
                print(f"[SOCKET] Received: {command}")

                response = self.process_command(command)
                connection.sendall(response.encode("utf-8"))

        except socket.timeout:
             print(f"[SOCKET] Connection timeout: {address}")

        except Exception as error:
             print(f"[SOCKET] Error: {error}")

        finally:
            connection.close()
            print(f"[SOCKET] Client disconnected: {address}")

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(5)

        print(f"[SOCKET] TCP server running on {HOST}:{PORT}")

        while True:
            connection, address = server.accept()
            Thread(
                target=self.handle_client,
                args=(connection, address),
                daemon=True
            ).start()


def run_socket_server(ecu1_service=None, ecu2_service=None):
    socket_server = SocketServer(ecu1_service, ecu2_service)
    socket_server.start()


if __name__ == "__main__":
    run_socket_server()