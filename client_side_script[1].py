from socket import *
def getIpAndPort():
	ip = input("Enter ip address: ")
	return ip, 50007
def getMessage(message):
	return message
def setSocketObject():
	socket_object = socket(AF_INET, SOCK_STREAM)
	return socket_object
def connectAndSendMessage(socket_object, ip, port, message):
	socket_object.connect((ip, port))
	for line in message:
		socket_object.send(line)
		data = socket_object.recv(1024)
		print(data)
	socket_object.close
def runClient():
	ip, port = getIpAndPort()
	message = getMessage([b'ghdjdjfjb'])
	socket_object = setSocketObject()
	connectAndSendMessage(socket_object, ip, port, message)
runClient()