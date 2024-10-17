import time
from socket import *
from datetime import datetime

# Server address and port
server_addr = ('localhost', 12000)
# Number of pings to send
num_pings = 20
# Timeout in seconds
timeout = 2

# Create UDP client socket
client_socket = socket(AF_INET, SOCK_DGRAM)
# Set socket timeout
client_socket.settimeout(timeout)

for seq_num in range(1, num_pings + 1):
    # Get current time in a readable format
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create ping message
    message = f"Ping {seq_num} {current_time}"
    
    try:
        # Send ping and record time
        send_time = time.time()
        client_socket.sendto(message.encode(), server_addr)
        
        # Receive response
        responseMessage, server = client_socket.recvfrom(1024)
        recv_time = time.time()
        
        # Calculate and print RTT
        rtt = recv_time - send_time
        print(responseMessage.decode())
        print(f"RTT: {rtt:.6f} seconds")
        
    except TimeoutError:
        print("Request timed out")
    
    # Wait a bit before sending the next ping
    time.sleep(0.1)

# Close the socket
client_socket.close()