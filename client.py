import socket
import os

BUFFER_SIZE = 2048
SEPARATOR = "-"
HOST = "192.168.56.1"
PORT = 6666
filename = "movies_info.csv"
filesize = os.path.getsize(filename)


def client_prog():
    client_socket = socket.socket()
    print("CONNECTING TO", HOST, ":", PORT)
    client_socket.connect((HOST, PORT))
    print("CONNECTED")

    send_str = filename+SEPARATOR+str(filesize)
    send_str = send_str.encode()
    client_socket.send(send_str)


    with open(filename, "rb") as f:
        
        while True:
            
            bytes_read = f.read(BUFFER_SIZE)
            
            if not bytes_read:
                break
            
            client_socket.sendall(bytes_read)
            
    client_socket.close()

if __name__ == "__main__":
    client_prog()