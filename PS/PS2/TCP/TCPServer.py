from socket import *

# calculate reward based on input string variable
def calculate_reward(string):    
    if string == 'A':
        return 3
    elif string == 'B':
        return 2
    elif string == 'C':
        return 1
    else:
        return -1
    
# set up local port number
serverPort = 15000

# create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
# bind socket to local port number 15000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    # wait for a client connection
    connectionSocket, addr = serverSocket.accept()

    # receive the string from the client and calculate the reward
    string = connectionSocket.recv(1024).decode().strip()
    reward = calculate_reward(string)
    # send back the reward
    connectionSocket.send(str(reward).encode())

    connectionSocket.close()