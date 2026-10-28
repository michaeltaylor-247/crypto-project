import socket
from threading import Thread
from datetime import datetime

TCP_IP = '0.0.0.0'  #server will listen for and accept connections from any IP address
TCP_PORT = 2004     #server port hardcoded for now
BUFFER_SIZE = 2048

# Multithreaded Python server 
class ClientThread(Thread):
    def __init__(self, conn, ip, port):
        Thread.__init__(self)
        self.conn = conn
        self.ip = ip
        self.port = port
        self.msgCount = 0
        print("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):
        while True:
            data = self.conn.recv(BUFFER_SIZE)
            if not data:        #client disconnected with "exit"
                break
            current_time = datetime.now().strftime("%H:%M:%S")
            print("Server recieved data:" + str(self.msgCount) + ":" + data.decode('utf-8') + ":" + current_time)
            MESSAGE = "Echo #" + str(self.msgCount) + ": " + data.decode('utf-8')
            self.conn.send(MESSAGE.encode('utf-8'))
            if data == b'exit':
                break
            self.msgCount += 1
        self.conn.close()
        print("Connection closed for "+ self.ip + ":" + str(self.port))

def main():
    tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpServer.bind((TCP_IP, TCP_PORT))
    tcpServer.listen(4)
    threads = []

    try:
        while True:
            print("Server : Waiting for connections from TCP clients...")
            (conn, (ip, port)) = tcpServer.accept()
            newthread = ClientThread(conn, ip, port)
            newthread.start()
            threads.append(newthread)
    except KeyboardInterrupt:
        print("\nServer shutting down")
    finally:
        tcpServer.close()

if __name__ == "__main__":
    main()
