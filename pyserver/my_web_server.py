import socket
import sys
from threading import Thread

def handle_client(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        if not message:
            return
        filename = message.split()[1]
        with open(filename[1:], 'r') as f:
            outputdata = f.read()

        #send HTTP OK Header
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

    except IOError:
        # Send HTTP response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>".encode())
    
    finally:
        #closing the client socket
        connectionSocket.close()



def start_server(serverPort=6789):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    print(f'The server is ready to receive on port {serverPort}')

    while True:
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        client_thread = Thread(target=handle_client, args=(connectionSocket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
