#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

server_address='localhost'
server_port=1234
print("Server connected")


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("WELCOME....!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    print("NAME: "+name)
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome.encode("utf8")))
    msg = "%s has joined the chat!" % name
    print(msg)
    broadcast(msg,name+" :")
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ).decode('utf8')
        print(name+": "+msg)
        if msg != bytes("{quit}".encode("utf8")):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}".encode("utf8")))
            client.close()
            del clients[client]
            broadcast("%s has left the chat." % name.encode("utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    print(msg+prefix)
    """Broadcasts a message to all the clients."""
    for client in clients:
        client.send(bytes((prefix+msg).encode('utf8')))

        
clients = {}
addresses = {}

BUFSIZ = 1024
ADDR = (server_address, server_port)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
SERVER.close()
