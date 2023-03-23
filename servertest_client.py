import io
import socket
import struct
import time

import picamera2
import picamera2.array
# from adafruit_servokit import ServoKit

# ########## Gamepad connection test ##########
# kit = ServoKit(channels=16)

# adr = ('10.0.0.2', 5000)
# c = socket.socket()
# c.connect(adr)

# while True:
#     buf = c.recv(128)
#     msg = buf.decode('utf-8')
#     msg = msg.split('!')
#     msg = msg[0]
#     if not msg:
#         pass
#     elif msg == 'shutdown':
#         break
#     elif msg.startswith('ABS_RY'):
#         print(msg)
#         msg = msg.split(' ')
#         val = int(msg[1])
#         val = val/32767*180
#         if val < 0:
#             val = 0
#         elif val > 180:
#             val = 180
#         kit.servo[0].angle = val
#     else:
#         print(msg)
#     # return_msg = 'Message recieved'
#     # return_msg = return_msg.encode('utf-8')
#     # c.send(return_msg)
# c.close()
# ########## /Gamepad connection test ##########

########## Imaging test ##########
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24
# rawCapture = picamera.array.PiRGBArray(camera, size=(640,480))

camera.start_preview()

adr = ('10.0.0.2', 5000)
client = socket.socket()
client.connect(adr)

connection = client.makefile('wb')
framecount = 0
try:    
    camera.start_recording(connection, format='h264')
    camera.wait_recording(10)
    camera.stop_recording()
finally:
    connection.close()
    client.close()