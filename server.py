import socket
import os

# Device's IP address
SERVER_HOST = "192.168.56.1"
# SERVER_HOST = "122.184.65.66"
# SERVER_HOST = "0.0.0.0"
SERVER_PORT = 6666
# receive 4096 bytes each time
BUFFER_SIZE = 2048
SEPARATOR = "-"

def server_prog():
    server_socket = socket.socket()
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    server_socket.listen(6)
    print("LISTENING AS ",SERVER_HOST,":",SERVER_PORT)

    client_socket, ADDRESS = server_socket.accept()

    print(ADDRESS, "IS CONNECTED")

    received = client_socket.recv(BUFFER_SIZE).decode()

    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)

    with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(2048)
            if not bytes_read:    
                break
            f.write(bytes_read)
            
    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    server_prog()