import socket
import time

import numpy as np
import picamera2

# rov_ip = "10.0.0.1"
# rov_port = 5000

# img_x = 800
# img_y = 600
# bitrate = 10000000

# cam = picamera2.Picamera2()
# cam.video_configuration.size = (img_x, img_y)
# cam.video_configuration.controls.FrameRate = 25.0
# cam.configure('video')

# encoder = picamera2.encoders.H264Encoder()
# cam.encoder = encoder

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     sock.bind((rov_ip, rov_port))
#     sock.listen()
#     print('Waiting for connection...')
    
#     conn, addr = sock.accept()
#     print('Connection established. Beginning stream...')
#     stream = conn.makefile('wb')
#     cam.encoder.output = picamera2.outputs.FileOutput(stream)
#     cam.start_encoder()
#     cam.start()
#     time.sleep(15)
#     cam.stop()
#     cam.stop_encoder()
#     print('Ending stream.')
#     conn.close()
# print('All connections closed. Shutting down ROV server.')


import io

BUFF_SIZE = 65536
img_x = 800
img_y = 640

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = '10.0.0.1'
port = 5000
socket_address = (host_ip,port)
server_socket.bind(socket_address)

cam = picamera2.Picamera2()
cam.still_configuration.size = (img_x, img_y)
cam.configure('still')

cam.start()

print('Listening at:',socket_address)


msg,client_addr = server_socket.recvfrom(BUFF_SIZE)
print('GOT connection from ',client_addr)

for frames in range(1, 50):
    img_buffer = io.BytesIO()
    cam.capture_file(img_buffer, format='jpeg')
    img_buffer.seek(0)
    while True:
        message = img_buffer.read(65507)
        if not message:
            break
        print('message size: {}'.format(len(message)))
        server_socket.sendto(message, client_addr)
    time.sleep(1/25)

server_socket.sendto(b'', client_addr)    
cam.stop()
server_socket.close()
print('ROV server shut down.')