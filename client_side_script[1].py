from socket import *
def getIpAndPort():
	ip = "192.168.0.24"
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
def restartMeesgae():
	return b'restart'
def shtudowm():
	return b'shutdown'
def sendMessageToServer(message_to_server):
	ip, port = getIpAndPort()
	#message = getMessage([message_to_server)
	socket_object = setSocketObject()
	connectAndSendMessage(socket_object, ip, port, message_to_server)
sendMessageToServer([b'restart'])