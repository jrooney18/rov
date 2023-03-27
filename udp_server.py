import socket
import time

UDP_IP = "10.0.0.2"
UDP_PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        if not data:
            break
