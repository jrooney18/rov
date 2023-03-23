import io
import socket
import struct
import subprocess

import numpy as np
import cv2 as cv
import inputs


# ########## Gamepad connection test ##########
# addr = ("", 5000)  # all interfaces, port 5000
# s = socket.socket()
# s.bind(addr)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.listen(1)
# client, addr = (s.accept())
# print('Connected to ' + str(client))
# print('Waiting for input...')

# while True:
#     is_pressed = False
#     msg = ''
#     buf = b''
    
#     events = inputs.get_gamepad()
#     for event in events:
#         if event.code == 'BTN_SOUTH' and event.state == 1:
#             print('X button pressed. Transmitting...')
#             #is_pressed = True
#             msg = 'X button pressed'
#         elif event.code == 'BTN_NORTH' and event.state == 1:
#             msg = 'shutdown'
#             is_pressed = True
#         elif event.code == 'ABS_RY':
#             msg = event.code + ' ' + str(event.state)
#     msg += '!'
#     buf = msg.encode('utf-8')
#     client.send(buf)
#     if is_pressed:
#         break
# ########## /Gamepad connection test ##########

########## Imaging test ##########
cmdline = [r'C:\Program Files\VideoLAN\VLC\vlc.exe', '--demux', 'h264', '-']
player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
addr = ("", 5000)
s = socket.socket()
s.bind(addr)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(0)

client = s.accept()[0].makefile('rb')
print('Connection to client established.')
try:
    while True:
        data = client.read(1024)
        if not data:
            break
        player.stdin.write(data)
        data_old = data
finally:
    client.close()
    s.close()
    player.terminate()
########## /Imaging test ###########

# return_msg = client.recv(4096)
# print(return_msg)
# s.close()