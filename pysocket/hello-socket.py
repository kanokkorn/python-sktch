import socket

host = "127.0.0.1"
port = 34567

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
  soc.bind((host, port))
  soc.listen()
  conn, addr = soc.accept()
  with conn:
    print("Connected by", addr)
    while True:
      data = conn.recv(1024)
      if not data:
        break
      conn.sendall(data)

