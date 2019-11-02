import socket
import util


def encodeData(data, key):
    """
    Returns:
    """
    remainder = util.dataCapsulation(data, key)

    codeword = data + remainder

    return codeword


s = socket.socket()
port = 12345
s.connect(("127.0.0.1", port))

input_string = input("Enter data you want to send:\n---> ")
data = ("".join(format(ord(x), 'b') for x in input_string))
key = "1001"
print("Raw data to send: ", data)

ans = encodeData(data, key)
print("Encoded data ready to send: " + ans)

s.sendall(ans.encode())

reply = s.recv(1024)
print(reply.decode())

s.close()
