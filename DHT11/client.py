import socket
f=open("test",'r')
a=f.read()
s=socket.socket()
host = '192.168.1.147'
port =12345
s.connect((host,port))
while True:
	s.send("hello\r\n")
print s.recv(1024)
s.close()
