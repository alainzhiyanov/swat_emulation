# client.py

import socket
import sys

def main(server_ip, value):
    server_port = 12345

    try:
        # Initialize client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        print("Connected to server at {}:{}".format(server_ip, server_port))

        # Send the value to the server
        client_socket.sendall(value)
        print("Sent: {}".format(value))

    except Exception as e:
        print("Error: {}".format(e))
    finally:
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_ip> <value>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
