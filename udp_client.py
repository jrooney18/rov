import socket

UDP_IP = "10.0.0.2"
UDP_PORT = 5000
MESSAGE = b"Hello, world"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

sock.close()