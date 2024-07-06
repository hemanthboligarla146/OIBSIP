import socket
conn = True
while conn:
    c = socket.socket()
    c.connect(('localhost',9992))
    msg = input('enter your message : ').lower()
    c.send(bytes(msg,'UTF-8'))
    if (msg == "close"):
        c.close()
        print("The chatting application is ended..!")
        break
    recvdmsg = c.recv(1024).decode()
    print(f"Server: {recvdmsg}")


