#Imports
import socket

#Constants
HOST = '127.0.0.1'
PORT = 1234
CLIENT_LIMIT = 2


def main():
    # AF_NET - IPv4
    # SOCK_STREAM - TCP Package
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # Exception Handling
    try:
        server.bind((HOST,PORT))
        print(f"Server running on {HOST} {PORT}")
    except:
        print(f"Unable to bind host {HOST} and port {PORT}")

    # Defining the Server Limit
    server.listen(CLIENT_LIMIT)

    # Keep Listening to Clients
    while 1 :
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")

if __name__ == '__main__':
    main()
