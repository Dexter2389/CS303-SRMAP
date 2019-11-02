import socket
import util

def decodeData(data, key):
    """
    Return:
    """
    remainder = util.dataCapsulation(data, key)
    return remainder

s = socket.socket()
print("Socket successfully created")

port = 12345

s.bind(('', port))
print("socket binded to %s" % (port))

s.listen(5)
print("socket listening")

x = 1
while x == 1:
    c, addr = s.accept()
    print("Got connection from ", addr)

    data = c.recv(1024)

    data = data.decode()
    print(data)

    if not data:
        break

    key = "1001"

    ans = decodeData(data, key)
    print("Remainder after decoding: " + ans)

    temp = "0" * (len(key) - 1)
    if ans == temp:
        msg = "Data recieved successfully without errors"
        c.sendall(msg.encode())
    else:
        msg = "Error"
        c.sendall(msg.encode())

    c.close()
    x += 1