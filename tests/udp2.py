#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("google.com", 53)

s.bind(("192.168.1.199",1123))
s.sendto(b"nmsl",addr)
response, addr = s.recvfrom(1024)
print(response)
print(addr)
print(response.decode())
s.close()