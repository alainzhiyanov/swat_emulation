import socket

def main():
    SERVER_IP = "0.0.0.0"  # Listen on all interfaces
    SERVER_PORT = 12345
    OUTPUT_FILE = "./P1-P101-DI_Run.txt"

    try:
        # Initialize server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse the address
        server_socket.bind((SERVER_IP, SERVER_PORT))
        server_socket.listen(5)  # Allow up to 5 queued connections
        print("Server listening on {}:{}".format(SERVER_IP, SERVER_PORT))

        while True:
            # Accept a new client connection
            conn, addr = server_socket.accept()
            print("Connected by {}".format(addr))

            try:
                # Receive data from the client
                data = conn.recv(1024)
                if data:
                    value = data.strip()
                    print("Received: {}".format(value))
                    # Write the value to a file
                    with open(OUTPUT_FILE, "w") as file:
                        file.write(value)
            except Exception as e:
                print("Error during client communication: {}".format(e))
            finally:
                conn.close()  # Close the connection with the current client
                print("Connection with {} closed.".format(addr))

    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as e:
        print("Server error: {}".format(e))
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
