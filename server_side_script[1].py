from socket import *
def getIpAndPort(ip_address, port_number):
	return ip_address, port_number
def setSocketObject(ip_address, port_number):
	socket_object = socket(AF_INET, SOCK_STREAM)
	socket_object.bind((ip_address, port_number))
	socket_object.listen(5)
	return socket_object
def receiveDataAndRespond(connection_object, response_message):
	while True:
		data = connection_object.recv(1024)
		if not data:
			break
		connection_object.send(response_message)
	connection_object.close()
def listenForRequest(socket_object):
	while True:
		connection_object, address = socket_object.accept()
		print("Connection from: ", address)
		receiveDataAndRespond(connection_object, "timer received")
def runServer():
	ip_address, port_number = getIpAndPort("", 50007)
	socket_object = setSocketObject(ip_address, port_number)
	listenForRequest(socket_object)
runServer()