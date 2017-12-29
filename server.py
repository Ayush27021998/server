from socket import *
import threading

s= socket(AF_INET,SOCK_STREAM)

host= ""
port= 5000


s.bind((host, port))
s.listen(1)
print("Server Ready")
conn,addr = s.accept()
print("Connected")

def goto(linenum):
    global line
    line = linenum

class Rocky_recieve(threading.Thread):
    def run(self):
        x=True
        while x==True:
            data = conn.recv(1024)
            print(data.decode())
            if not data:
                goto(11)
                break






class Rocky_send(threading.Thread):
    def run(self):
        while True:
            mess = "Server --> "+input()
            conn.send(mess.encode())

x=Rocky_recieve()
y=Rocky_send()
x.start()
y.start()


