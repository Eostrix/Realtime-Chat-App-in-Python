# Imports
import socket
import threading

#Constants
HOST = '127.0.0.1'
PORT = 1234

def communicateToServer(client):
    username = input("State your username: ")
    if username != '':
        client.sendall(username.encode())
        print(f"welcome aboard {username}, you are good to go...")
    
    threading.Thread(target=listenFromServer, args=(client, )).start()
    sendToServer(client)

def listenFromServer(client):
    # Fetching other Clients' msg from server
    while 1:
        content = client.recv(1024).decode('utf-8')
        if content != '':
            newContent = content.split('~')
            username = newContent[0]
            msg = newContent[1]
            print(f"[{username}] {msg}")

def sendToServer(client):
    # Client msg to server
    while 1:
        msg = input("")
        if msg != '':
            client.sendall(msg.encode())

def main():
    # AF_NET - IPv4
    # SOCK_STREAM - TCP Package
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # Exception Handling
    try:
        client.connect((HOST,PORT))
        print("// Connected to the server successfully")
    except:
        print(f"Unable to connect to the server {HOST} {PORT}")
    
    communicateToServer(client)

if __name__ == '__main__':
    main()