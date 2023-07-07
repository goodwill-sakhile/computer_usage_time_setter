from socket import *
from commands_script import *
def getIpAndPort(ip_address, port_number):
	return ip_address, port_number
def setSocketObject(ip_address, port_number):
	socket_object = socket(AF_INET, SOCK_STREAM)
	socket_object.bind((ip_address, port_number))
	socket_object.listen(5)
	return socket_object
def executeClientMessage(message):
	if message == b'shutdown':
		shutDownTerminal()
	elif message == b'restart':
		
		restartTerminal()
def receiveDataAndRespond(connection_object, response_message):
	while True:
		data = connection_object.recv(1024)
		if not data:
			break
		print(data)
		executeClientMessage(data)
		connection_object.send(response_message)
	connection_object.close()
def listenForRequest(socket_object):
	while True:
		print("Server is listening:")
		connection_object, address = socket_object.accept()
		print("Connection from: ", address)
		receiveDataAndRespond(connection_object, b'timer received'')
def runServer():
	ip_address, port_number = getIpAndPort("", 50007)
	socket_object = setSocketObject(ip_address, port_number)
	listenForRequest(socket_object)
runServer