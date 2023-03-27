import socket
import time

UDP_IP = "10.0.0.1"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    localtime = time.time_ns()
    data, addr = sock.recvfrom(1024)
    break
    
sock.close()

sendtime = data.decode('utf-8')
diff = (localtime - int(sendtime))/1e9
print('Time difference: {}'.format(diff))