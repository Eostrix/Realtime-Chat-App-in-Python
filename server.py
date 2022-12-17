#Imports
import socket
import threading

#Constants
HOST = '127.0.0.1'
PORT = 1234
CLIENT_LIMIT = 5    # Maximum connections to the server
activeClients = []

def clientHandler(client):
    # waiting for client to join
    while 1:
        username = client.recv(32).decode('utf-8') # username max len is 32
        if username != '':
            activeClients.append((username,client)) # appending current client to the active list
            announcement = f"SERVER~// {username} has joined the chat! //"
            sendMsgToAll(announcement,client)
            break;

    threading.Thread(target=listenFromClient, args=(client,username,)).start()

def listenFromClient(client, username):
    # waiting for client to send msgs
    while 1:
        msg = client.recv(1024).decode('utf-8') # msg len max 1024 character
        if msg != '' :
            modifiedMsg = username + '~' + msg
            sendMsgToAll(modifiedMsg,client) 

def sendMsgToAll(msg,client):
    # Broadcasting msg to all active clients except the sender
    for user in activeClients:
        if user[1] != client : 
            sendMsgToIndividual(user[1], msg)

def sendMsgToIndividual(client, msg):
    # Sending msg to individual
    client.sendall(msg.encode())

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
        print(f"Connection to client successful {address[0]} {address[1]}")

        threading.Thread(target=clientHandler, args=(client,)).start()

if __name__ == '__main__':
    main()
