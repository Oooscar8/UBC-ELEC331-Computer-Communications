from socket import *

# set up server hostname and port number
serverName = 'localhost'
serverPort = 15000

# Run indefinitely to allow continuous client-server communication
while True:
    # create a TCP socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # connect to server at the specified hostname and port
    clientSocket.connect((serverName, serverPort))

    string = input('Input the string variable:')
    clientSocket.send(string.encode())

    # receive the reward from the server
    reward = clientSocket.recv(1024)
    print(reward.decode())
    clientSocket.close()