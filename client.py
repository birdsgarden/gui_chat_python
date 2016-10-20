#!/bin/python
__author__ = 'cxtan'
import socket
import sys, os
import time

def TCP_connect():
    name = raw_input("input name:")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("192.168.4.16", 9999))
    sock.send(name)
    data = sock.recv(1024)
    print data
    name = name + ":"
    while True:
        in_data = raw_input(name)
        sock.send(in_data)
        if in_data == "exit":
            break
    sock.close()
if __name__ == '__main__':
    TCP_connect()
    pass

































