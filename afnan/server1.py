# Task 03 Client Server Communication
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1024))
s.listen(5)
while True:
	clt, adr=s.accept()
	print("Connection to {adr} established")
	mssg = "Socket Programming in Python"
	clt.send((bytes(mssg, "utf-8")))
	clt.close()