# UDP Pinger Lab

This lab demonstrates how to implement a simple UDP Ping client and server in Python.

## Files
- `UDPPingerServer.py` : The UDP ping server. You do not need to modify this file.
- `UDPPingerClient.py` : The UDP ping client. This is your implementation.

## How to Run
1. Open a terminal and run the server:
   ```bash
   python UDPPingerServer.py
   ```

2. Open another terminal and run the client:
   ```bash
   python UDPPingerClient.py
   ```

3. The client will send 10 ping messages to the server.
- If the server replies, you will see the reply message and round-trip time (RTT).
- If the packet is lost, you will see "Request timed out".

## Notes
- The server simulates about 30 percent packet loss.
- RTT values are measured in seconds.
- The output includes the ping number, reply messages, and RTT for each successful ping.
- Since the server randomly drops packets, the number of timeouts may vary between runs.
