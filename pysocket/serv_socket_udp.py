import socket
import time

servsoc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servsoc.bind(('', 12000))

data = ['apple', 'banana', 'orange', 'pineapple', 'peach']

msg, addr = servsoc.recvfrom(1024)

for msgr in data:
  msg_enc = str.encode(msgr) 
  servsoc.sendto(msg_enc, addr)
  time.sleep(1)