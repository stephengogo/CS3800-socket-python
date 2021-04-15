#April 15th In Class
#server.py 


# import socket
# # create a socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #bind the socket to host and port
# #hostname = 172.0.0.1
# s.bind((socket.gethostname(), 9999))
# s.listen()

# while True:
#     clientsocket, address = s.accept()
#     print(f"Connection from {address} has been established.")
#     clientsocket.send(bytes("Hello Wolrd!"))
#     clientsocket.close()

# Code above not working 
# Try: https://pythonprogramming.net/sockets-tutorial-python-3/

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()
host = '127.0.0.1'
s.bind((host, 1234))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Hey there!!!","utf-8"))

