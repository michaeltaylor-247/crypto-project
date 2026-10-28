#Dr. Marian Zaki - CSCE 449 Applied Cryptography
#Simple Client Application uses TCP sockets to send data to a server
#Note the code isn't well structured - for example: hard coded port numbers! This is just something to get you started
import socket

HOST = socket.gethostname()
PORT = 2004  #server port
BUFFER_SIZE = 2048

def main():
    tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        tcpClient.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Could not connect to server at " + str(HOST) + ":" + str(PORT) + ". Is it running?")
        return

    try:
        while True:
            MESSAGE = input("Client: Enter message to continue/ Enter exit:")
            if not MESSAGE:          # don't send empty messages
                continue
            tcpClient.send(MESSAGE.encode('utf-8'))
            data = tcpClient.recv(BUFFER_SIZE)
            if not data:             # server closed the connection
                print("Server closed the connection")
                break
            print("Client received data:", data.decode('utf-8'))
            if MESSAGE == 'exit':
                break
    except (KeyboardInterrupt, ConnectionResetError, BrokenPipeError):
        print("\nConnection ended")
    finally:
        print("Client Terminating")
        tcpClient.close()


if __name__ == "__main__":
    main()