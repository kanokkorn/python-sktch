import socket 

host = "127.0.0.1"
port = 34567

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
  soc.connect((host, port))
  soc.sendall(b"Hello world")
  data = soc.recv(1024)

print("Received ", repr(data))

