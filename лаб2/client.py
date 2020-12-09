import socket
from json import loads as json_to_dict,dumps as dict_to_json
from time import time,ctime,sleep

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(10)]

for i in range(10):
    client[i].connect((socket.gethostname(), 1234))
    client[i].send(bytes(dict_to_json({"ID": i,"Surname": "Surname"}),"utf-8") )         #udalit utf8

for i in range(10):
    while True:
        data = client[i].recv(4000)
        data1 = data.decode("utf-8")
        print("User", i, ".")
        print("Conections:")
        for o in range(10):
            print(data1[o]["ID"], 
                  data1[o]["Surname"],
                  ctime(data1[o]['date']),
                  ctime(data1[o]['timer_start']))
        break