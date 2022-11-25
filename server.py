import socket
import os

# Device's IP address
# SERVER_HOST = "192.168.56.1"
# SERVER_HOST = "122.184.65.66"
SERVER_HOST = "10.59.232.84"
# SERVER_HOST = "0.0.0.0"
SERVER_PORT = 6666

BUFFER_SIZE = 9216
SEPARATOR = "-"

def server_prog():
    server_socket = socket.socket()
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    server_socket.listen(6)
    print("LISTENING AS ",SERVER_HOST,":",SERVER_PORT)

    client_socket, ADDRESS = server_socket.accept()

    print(ADDRESS, "IS CONNECTED")

    filename = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    print("FILENAME IS ", filename)
    file = open(filename, "w")
    client_socket.send("FILE NAME RECIEVED".encode("utf-8"))


    data = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    print("Length of the data recieved :- ",len(data))
    file.write(data)
    client_socket.send("DATA RECIEVED".encode("utf-8"))
    
    print("File recieved and read")        
    client_socket.close()
    print("FILE TRANSFER DONE")
    server_socket.close()
    print("DISCONNECTED")


if __name__ == "__main__":
    server_prog()