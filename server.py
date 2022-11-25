import socket
import os

# Device's IP address
# SERVER_HOST = "192.168.56.1"
# SERVER_HOST = "122.184.65.66"
SERVER_HOST = "10.59.232.84"
SERVER_HOST = '''Device's IP address'''
# SERVER_HOST = "0.0.0.0"
SERVER_PORT = 6666
BUFFER_SIZE = 9216


def server_prog():
    # Creating a server socket to recieve the data
    server_socket = socket.socket()

    # making a server socket
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    # 6 unaccepted connections that the system will allow before refusing new connections.
    server_socket.listen(6)
    print("LISTENING AS ",SERVER_HOST,":",SERVER_PORT)

    # Accepting the connection made
    client_socket, ADDRESS = server_socket.accept()

    print(ADDRESS, "IS CONNECTED")

    filename = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    print("FILENAME IS ", filename)
    file = open(filename, "w")
    # After the filename was succesfully recieved, server opens a new file with same filename and sends a message
    client_socket.send("FILE NAME RECIEVED".encode("utf-8"))

    # Recieving the data from sender(client socket)
    data = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    print("Length of the data recieved :- ",len(data))
    # Writing that daat into the file opened
    file.write(data)
    client_socket.send("DATA RECIEVED".encode("utf-8"))
    
    # Closing the sockets after sucessfull data transfer
    print("File recieved and read")        
    client_socket.close()
    print("FILE TRANSFER DONE")
    server_socket.close()
    print("DISCONNECTED")


if __name__ == "__main__":
    server_prog()