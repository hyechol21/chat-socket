
import socket


SERVER = "192.168.0.69"
PORT = 5050
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECTED_MESSAGE = "!DISCONNECT"

c_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
c_sock.connect(ADDR)

def send():
    # 닉네임 설정
    nickname = input("Your Nickname: ")
    c_sock.send(nickname.encode(FORMAT))

    while True:
        conn_data = c_sock.recv(1024).decode(FORMAT)
        if conn_data:
            print(conn_data, end='\n\n') # 접속중인 사람 표시

        sendto_nickname = c_sock.send(input('받을 사람: '))
        msg = input("보낼 메시지> ")
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))

        c_sock.send(send_length)
        c_sock.send(message)

        # print(c_sock.recv(1024).decode(FORMAT))

send()