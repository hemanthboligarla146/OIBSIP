import socket
# function used to check and exit the application
def checkConnection(msg):
    if(msg== "close"):
        c.close()
        s.close()
        print("The chatting applicatipn is ended..!")
        return True
    return False

s = socket.socket()
print('Server created')
s.bind(('localhost', 9992))
s.listen(1)
print('waiting for connection')
conn = True
while conn:
    c,addr = s.accept()
    recvdmsg = c.recv(1024).decode()
    if checkConnection(recvdmsg):
        break
    print(f"Client: {recvdmsg}")
    msg=input('enter server your message : ')
    c.send(bytes(msg,'UTf-8'))


