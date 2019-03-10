#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import socks

socks.set_default_proxy(socks.SOCKS5,"127.0.0.1",1080)
 
s = socks.socksocket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("1.1.1.1", 53)
 
s.sendto(b"nmsl",addr)
response, addr = s.recvfrom(1024)
print(response.decode())
s.close()