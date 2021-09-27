# 클라이언트

import socket


HEADER = 64
PORT= 5050
FORMAT = 'utf-8'
DISCONNECTED_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.69"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)