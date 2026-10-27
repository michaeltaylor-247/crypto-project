#Dr. Marian Zaki - CSCE 449 Applied Cryptography
#Simple Client Application uses TCP sockets to send data to a server
#Note the code isn't well structured - for example: hard coded port numbers! This is just something to get you started
import socket

host = socket.gethostname()
port = 2004  #server port
BUFFER_SIZE = 2000
#MESSAGE = input("Client: Enter message/ Enter exit:")
MESSAGE = ""
tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))

while MESSAGE != 'exit':
    MESSAGE = input("Client: Enter message to continue/ Enter exit:")
    MESSAGE_BYTES = bytes(MESSAGE, 'utf-8')
    tcpClient.send(MESSAGE_BYTES)
    data = tcpClient.recv(BUFFER_SIZE)
    print("Client received data:", str(data))

print("Client Terminating")
tcpClient.close()