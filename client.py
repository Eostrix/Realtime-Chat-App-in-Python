# Imports
import socket

#Constants
HOST = '127.0.0.1'
PORT = 1234

def main():
    # AF_NET - IPv4
    # SOCK_STREAM - TCP Package
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # Exception Handling
    try:
        client.connect((HOST,PORT))
        print("Successfully connected to the server")
    except:
        print(f"Unable to connect to the server {HOST} {PORT}")

if __name__ == '__main__':
    main()