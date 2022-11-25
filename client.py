import socket
import os

BUFFER_SIZE = 9216
# HOST = "192.168.56.1"
# HOST = "122.184.65.66"
HOST = "10.59.232.84"

PORT = 6666
filename = "movies_info.csv"
filesize = os.path.getsize(filename)


def client_prog():
    client_socket = socket.socket()
    print("CONNECTING TO", HOST, ":", PORT)
    client_socket.connect((HOST, PORT))
    print("CONNECTED")

    file = open(filename, "r")
    data = file.read()
    print(len(data))
    
    client_socket.send(filename.encode("utf-8"))
    msg1 = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    print("SERVER SAYS :- ", msg1)

    
    client_socket.send(data.encode("utf-8"))
    msg2 = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    print("SERVER SAYS :- ", msg2)

    file.close()

            
    print("ALL THE CONTENTS OF THE FILES HAS BEEN SENT")
    client_socket.close()
    print("DISCONNETED")

if __name__ == "__main__":
    client_prog()