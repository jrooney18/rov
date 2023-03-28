import socket
import subprocess
import time

import cv2 as cv
import numpy as np

# rov_ip = "10.0.0.1"
# rov_port = 5000

# cmdline = [r'C:\Program Files\VideoLAN\VLC\vlc.exe', '--demux', 'jpg', '-']
# player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#     sock.connect((rov_ip, rov_port))
#     while True:
#         data, addr = sock.recvfrom(1024)
#         if not data:
#             break
#         player.stdin.write(data)

# player.terminate()


BUFF_SIZE = 65536
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = '10.0.0.1'
port = 5000
message = b'Hello'

client_socket.sendto(message,(host_ip,port))

while True:
    packet,_ = client_socket.recvfrom(BUFF_SIZE)
    npdata = np.fromstring(packet, dtype=np.uint8)
    frame = cv.imdecode(npdata, 1)
    cv.imshow("Video", frame)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        client_socket.close()
        break