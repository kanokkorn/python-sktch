import socket

host = "127.0.0.1"
port = 34567

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
  soc.bind((host, port))
  while True:
    soc.listen()
    conn, addr = soc.accept()
    print("Connected by", addr)
    data = conn.send(bytes("Hello", "utf-8"))

