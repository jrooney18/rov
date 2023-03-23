import socket
import os
import random
import time

import inputs

key_events = {
    'BTN_SOUTH': 'X button',
    'BTN_NORTH': 'Triangle button',
    'BTN_EAST': 'Circle button',
    'BTN_WEST': 'Square button',
    'BTN_TL': 'Left trigger button',
    'BTN_TR': 'Right trigger button',
    'BTN_START': 'Share button',
    'BTN_SELECT': 'Options button',
    'BTN_THUMBL': 'Left thumb stick',
    'BTN_THUMBR': 'Right thumb stick',
    'ABS_HAT0X': 'D-pad l-R',
    'ABS_HAT0Y': 'D-pad U-D'
    }

while True:
    events = inputs.get_gamepad()
    for event in events:
        if event.ev_type == 'Key' and event.state == 1:
            print(f'{key_events[event.code]} pressed')
        if event.code == 'ABS_HAT0X':
            if event.state == -1:
                print('D-pad L pressed')
            if event.state == 1:
                print('D-pad R pressed')
        if event.code == 'ABS_HAT0Y':
            if event.state == -1:
                print('D-pad U pressed')
            if event.state == 1:
                print('D-pad D pressed')
        if event.ev_type == 'Absolute' and event.code == 'ABS_RX':
            rx = event.state/32767
        ### Other sticks eliminated for clarity: ABS_RY, ABS_X, and ABS_Y ###
        ### Joystick resolution from -32767 - 32767 ###