# UDPPingerClient.py
import time
from socket import *

# Server details
serverName = '127.0.0.1'  # localhost for testing
serverPort = 12000

# Create UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)  # 1 second timeout

# Send 10 pings
for i in range(1, 11):
    # Prepare message
    send_time = time.time()
    message = f"Ping {i} {send_time}"
    try:
        # Send to server
        clientSocket.sendto(message.encode(), (serverName, serverPort))

        # Receive response
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        recv_time = time.time()
        rtt = recv_time - send_time

        print(f"Ping {i}: Reply from {serverName}: {modifiedMessage.decode()} RTT = {rtt:.6f} sec")

    except timeout:
        print(f"Ping {i}: Request timed out")
