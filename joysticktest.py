import matplotlib.pyplot as plt
from time import sleep

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

rx = 0
ry = 0
lx = 0
ly = 0

fig, ax = plt.subplots(figsize=(8,8))
plt.axis([-1, 1, -1, 1])
plt.gca().set_aspect('equal')
(ptr,ptl,) = ax.plot(rx, ry, 'ro', lx, ly, 'bo', animated=True)

plt.show(block=False)
plt.pause(0.1)

bg = fig.canvas.copy_from_bbox(fig.bbox)
ax.draw_artist(ptr)
ax.draw_artist(ptl)
fig.canvas.blit(fig.bbox)

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
            ptr.set_xdata(rx)
        #     print('Right stick x-motion detected')
        #     #print(event.ev_type, event.code, event.state)
#        if event.ev_type == 'Absolute' and event.code == 'ABS_RY':
#            ry = event.state/32767
#            ptr.set_ydata(ry)
        #     print('Right stick y-motion detected')
        #     #print(event.ev_type, event.code, event.state)
#        if event.ev_type == 'Absolute' and event.code == 'ABS_X':
#            lx = event.state/32767
#            ptl.set_xdata(lx)
        #     print('Left stick x-motion detected')
        #     #print(event.ev_type, event.code, event.state)
#        if event.ev_type == 'Absolute' and event.code == 'ABS_Y':
#            ly = event.state/32767
#            ptl.set_ydata(ly)
    fig.canvas.restore_region(bg)
    # re-render the artist, updating the canvas state, but not the screen
    ax.draw_artist(ptl)
    ax.draw_artist(ptr)
    # copy the image to the GUI state, but screen might not changed yet
    fig.canvas.blit(fig.bbox)
    # flush any pending GUI events, re-painting the screen if needed
    fig.canvas.flush_events()
    # you can put a pause in if you want to slow things down
    #plt.pause(1)
    #sleep(.05)