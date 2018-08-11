################## File 2: Receive side ##################################
# This simple python script receives UDP packets that arrive at port# 9002

import socket

rxSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rxSocket.bind(("127.0.0.1",9002))

while True:
   packet = rxSocket.recv(1024)
   print packet

###### End of File 2 ####################################################
