import socket
import os

print('Simple.py PID:' , os.getpid())
hostname = socket.gethostname()
print('Hostname:', hostname)
