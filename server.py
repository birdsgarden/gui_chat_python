#!/bin/python
__author__ = 'cxtan'

import socket
import os, sys
import threading
import time
def new_clint(client, addr):
    name = client.recv(1024)
    print "A new client connect server addr: %s:%s" % addr,
    print "client name %s:" % name
    client.send("welcome cxtan server %s" % name)
    while True:
        data = client.recv(1024)
        if data == 'exit' or not data:
            break
        print "%s:%s----->" % addr,
        print "%s: %s" % (name, data)
    client.close()
    pass

def server_end(local_ip):
    sock_ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_ser.bind((local_ip, 9999))
    sock_ser.listen(10)
    print "wait client connect......."
    while True:
        client, addr = sock_ser.accept()
        t = threading.Thread(target = new_clint, args = (client, addr))
        t.start()

if __name__ == '__main__':
    local_IP = socket.gethostbyname(socket.gethostname())
    server_end(local_IP)
    pass



































