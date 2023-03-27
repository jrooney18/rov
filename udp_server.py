import socket
import subprocess
import time

rov_ip = "10.0.0.1"
rov_port = 5000

cmdline = [r'C:\Program Files\VideoLAN\VLC\vlc.exe', '--demux', 'h264', '-']
player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((rov_ip, rov_port))
    while True:
        data, addr = sock.recvfrom(1024)
        if not data:
            break
        player.stdin.write(data)

player.terminate()
