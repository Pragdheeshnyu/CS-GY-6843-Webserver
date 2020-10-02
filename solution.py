#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    h, p = "127.0.0.1", port
    #serverSocket = socket()
    serverSocket.bind((h, p))
    serverSocket.listen(0)
    print('listening')
    while True:
        #Establish the connection
        connection, _ = serverSocket.accept()
        print('Ready to serve...')
        connectionSocket, addr = connection, "127.0.0.1"
        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            #print(filename)
            #print(f.read())
            outputdata = f.read()
            print(outputdata)
            # #Send one HTTP header line into socket
            # #Fill in start
            connectionSocket.send('HTTP/1.0 200 OK\r\n'.encode())
            # #Fill in end
            #
            # #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found (404)
            #Fill in start
            connectionSocket.send('HTTP/1.0 404 Not Found\r\n'.encode())
            #Fill in end

            #Close client socket
            #Fill in start
            connectionSocket.close()
            #Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
