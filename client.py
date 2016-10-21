#!/bin/python
__author__ = 'cxtan'
import socket, select
import sys, os
import time
import threading

def new_process(sock, read_in):
    while True:
        read_list, write_list, error_list = select.select(read_in, [], [])
        for cur_sock in read_list:
            if cur_sock == sock:
                data = cur_sock.recv(1024)
                if not data:
                    print "disconnect server"
                    sys.exit()
                else:
                    print data
def TCP_connect(local_IP):
    name = raw_input("input name:")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("192.168.4.3", 9999))
    sock.send(name)
    data = sock.recv(1024)
    print data
    name = name + ":\n"
    read_in = [sys.stdin, sock]
    t = threading.Thread(target = new_process, args = (sock, read_in))
    t.start()
    while True:
        in_data = raw_input(name)
        sock.send(in_data)
        if in_data == "exit":
            t.close()
            break

    sock.close()
if __name__ == '__main__':
    local_IP = socket.gethostbyname(socket.gethostname())
    TCP_connect(local_IP)
    pass

































