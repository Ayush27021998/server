from socket import *
import threading

s= socket(AF_INET,SOCK_STREAM)

host= "crimemastergogo.chickenkiller.com"
port= 5001

s.bind((host,port))

s.listen(1)
print('Server ready')

conn,addr= s.accept()
print("Connected")

class Rocky_recieve(threading.Thread):
    def run(self):
        while True:
            data = conn.recv(1024)
            print(data.decode())


class Rocky_send(threading.Thread):
    def run(self):
        while True:
            mess = "Server --> "+input()
            conn.send(mess.encode())

x=Rocky_recieve()
y=Rocky_send()
x.start()
y.start()


