import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 14900))
name = input("Select name : ")
id_ = input("Select id : ")
x = {"name" : name,"id" : id_}
send_json = json.dumps(x)
print("Sending %s" % send_json)
s.sendall(send_json.encode())
data = s.recv(1024)
s.close()
print('Received', repr(data))