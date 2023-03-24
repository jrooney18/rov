import io
import socket
import struct
import time

from picamera2 import Picamera2, encoders
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
camera = Picamera2()
camera.video_configuration.size = (800, 600)
camera.video_configuration.controls.FrameRate = 25.0
camera.configure("video")
# Consider adding fast noise reduction here, see "Configurations and runtime
# camera controls", Picamera2 manual p. 21

# camera.start_preview()

encoder = encoders.H264Encoder(bitrate=10000000)

adr = ('10.0.0.2', 5000)
client = socket.socket()
client.connect(adr)

connection = client.makefile('wb')
# framecount = 0
try:  
    camera.start_recording(connection, encoder)
    time.sleep(10)
    camera.stop_recording()
finally:
    connection.close()
    client.close()