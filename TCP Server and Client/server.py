import socket

s = socket.socket()
host = "127.0.0.1"
port = 8080

s.bind((host, port))

print("Waiting for connection...")
s.listen(5)

while True:
    conn, addr = s.accept()
    print("Connection established with ", addr)

    conn.send(b"Server Says Hi")
    conn.close()

