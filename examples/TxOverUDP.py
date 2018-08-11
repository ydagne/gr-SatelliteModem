################## File 1: Transmit side ################################
# This simple python script sends few UDP packets to port# 9001

import socket
import time

txSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for n in range(10):
   print "Sending: \"This a test message "+str(n)+ "\""
   txSocket.sendto("This a test message "+str(n), ("127.0.0.1", 9001))
   time.sleep(1)

# Flush the buffer
txSocket.sendto(" ", ("127.0.0.1", 9001))
time.sleep(1)
txSocket.sendto(" ", ("127.0.0.1", 9001))
# Packets larger than MTU will be truncated!
###### End of File 1 ####################################################
