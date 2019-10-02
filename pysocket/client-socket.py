import socket 

host = "127.0.0.1"
port = 34567

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
  soc.connect((host, port))
  data = soc.recv(102400)

print("Received ", repr(data))

