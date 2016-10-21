#!/bin/python
__author__ = 'cxtan'

import socket, select
import os, sys
import threading
import time
CONNECT_LIST = []
lock = threading.Lock()
def broadcast_data(sock, mesege, sock_ser):
    global CONNECT_LIST
    try:
        #lock.acquire()
        for client_sock in CONNECT_LIST:
            try:
                if client_sock != sock and client_sock != sock_ser:
                    print "broadcast_data to client"
                    client_sock.send(mesege)
            except:
                client_sock.close()
                CONNECT_LIST.remove(sock)
    finally:
        pass
        #lock.release()
    pass

def new_clint(sock_ser, client, addr, client_name):
    global CONNECT_LIST
    print "enter %s threading" % client_name
    while True:
        data = client.recv(1024)
        if data == 'exit' or not data:
            break
        data = "%s:%s----->" % addr + "%s: %s" % (client_name, data)
        broadcast_data(client, data, sock_ser)

    client.close()
    try:
        lock.acquire()
        CONNECT_LIST.remove(client)
    finally:
        lock.release()
    data = "Client %s(%s, %s) is offline" % (client_name, addr)
    broadcast_data(client, data, sock_ser)
    pass

def server_end(local_ip):
    global CONNECT_LIST
    sock_ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_ser.bind(("192.168.4.3", 9999))
    sock_ser.listen(10)
    CONNECT_LIST.append(sock_ser)
    print "wait client connect......."
    while True:
        read_socket, write_socket, error_socket = select.select(CONNECT_LIST, [], [])
        for sock in read_socket:
            if sock == sock_ser:
                client, addr = sock_ser.accept()
                client_name = client.recv(1024)
                print "A new client connect server addr: %s:%s" % addr,
                print "client name %s:" % client_name
                lock.acquire()
                try:
                    CONNECT_LIST.append(client)
                finally:
                    lock.release()
                for client_sock in CONNECT_LIST:
                    if client_sock != sock_ser:
                        client_sock.send("welcome cxtan server, %s" % client_name)
                t = threading.Thread(target = new_clint, args = (sock_ser, client, addr, client_name))
                t.start()



if __name__ == '__main__':
    local_IP = socket.gethostbyname(socket.gethostname())
    server_end(local_IP)
    pass



































