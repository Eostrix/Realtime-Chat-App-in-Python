# Imports
import socket
import threading

#Constants
HOST = '127.0.0.1'
PORT = 1234

def communicateToServer(client):
    username = input("Enter your username: ")
    if username != '':
        client.sendall(username.encode())
    
    threading.Thread(target=listenFromServer, args=(client, )).start()
    sendToServer(client)

def listenFromServer(client):
    while 1:
        content = client.recv(1024).decode('utf-8')
        if content != '':
            newContent = content.split('~')
            # print(newContent)
            username = newContent[0]
            msg = newContent[1]
            print(f"[{username}] {msg}")

def sendToServer(client):
    while 1:
        msg = input("Write your thoughts :")
        if msg != '':
            client.sendall(msg.encode())
        else:
            exit(0)

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
    
    communicateToServer(client)

if __name__ == '__main__':
    main()