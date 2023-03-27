import socket
import time

import picamera2

rov_ip = "10.0.0.1"
rov_port = 5000

img_x = 800
img_y = 600
bitrate = 10000000

cam = picamera2.Picamera2()
cam.video_configuration.size = (img_x, img_y)
cam.video_configuration.controls.FrameRate = 25.0
cam.configure('video')

encoder = picamera2.encoders.H264Encoder(bitrate=bitrate)
cam.encoder = encoder

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((rov_ip, rov_port))
    sock.listen()
    print('Waiting for connection...')
    
    conn, addr = sock.accept()
    print('Connection established. Beginning stream...')
    stream = conn.makefile('wb')
    cam.encoder.output = picamera2.outputs.FileOutput(stream)
    cam.start_encoder()
    cam.start()
    time.sleep(15)
    cam.stop()
    cam.stop_encoder()
    print('Ending stream.')
    conn.close()
print('All connections closed. Shutting down ROV server.')