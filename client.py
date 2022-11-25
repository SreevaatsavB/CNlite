import socket
import os

BUFFER_SIZE = 9216
# The reciever's (IPv4) address (of wireless connection)

HOST = '''Device's IP address'''

# Port number
PORT = 6666

# Filename of the file to be transferred
filename = "movies_info.csv"
def client_prog():

    # Creating a socket for the client to send the file
    client_socket = socket.socket()

    # Connecting to the server with TCP protocol
    print("CONNECTING TO", HOST, ":", PORT)
    client_socket.connect((HOST, PORT))
    print("CONNECTED")

    # reading the file 
    file = open(filename, "r")
    data = file.read()
    print("Length of data beign sent :-", len(data), "Bytes")
    # We use the utf-8 encoding and decoding to transfer data via TCPs

    # Sending file name to the server(reciever), so that it can save the data into that file    
    client_socket.send(filename.encode("utf-8"))
    # Reading the message Server sends
    msg1 = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    print("SERVER SAYS :- ", msg1)

    # Sending the data 
    client_socket.send(data.encode("utf-8"))
    # Reading the message Server sends
    msg2 = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    print("SERVER SAYS :- ", msg2)

    # Closing file after all the files contents have been sent
    print("ALL THE CONTENTS OF THE FILES HAS BEEN SENT")
    file.close()
        
    # Closing the client socket
    client_socket.close()
    print("DISCONNETED")

if __name__ == "__main__":
    client_prog()