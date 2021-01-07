import socket

def Server():
	global server

	Host, Port = '169.254.40.25', 6482

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((Host, Port))

def ListenAndAcceptConnection():
	global server, client
	server.listen()
	client, address = server.accept()
	client.send("\n\n			Server:	You just connected to the server ".encode('utf-8'))

def Listen():
	while True:

		CmdMode = False

		Server_Command_Recive = client.recv(1024).decode('utf-8')

		if Server_Command_Recive == "CmdOn":
			CmdMode = True
			client.send("\n\n			Server:	!! Cmd Mode Is On !!".encode('utf-8'))
			continue

		if Server_Command_Recive == "CmdOff":
			CmdMode = False
			client.send("\n\n			Server:	!! Cmd Mode Is Off !!".encode('utf-8'))

		if Server_Command_Recive == "Help" or Server_Command_Recive == "help":
			client.send("""\n\n
	*Avaiable commands:
	Help / help
	EXIT
	Disconnect
	CmdOn
	CmdOff
	""".encode('utf-8'))
			continue




		if Server_Command_Recive == "EXIT":
			client.send("\n\n			Server:	Confirm By Typing: 'Exit_Confirm_True'".encode('utf-8'))
			continue

		if Server_Command_Recive == "Exit_Confirm_True":
			client.send("\n\n			Server:	You closed server script".encode('utf-8'))
			exit()


		if Server_Command_Recive == "Disconnect":
			client.send("\n\n			Server:	You just disconnected".encode('utf-8'))
			client.close()
			ReStart()

		if CmdMode:
			CMD = os.system(Server_Command_Recive)
			#CMD = os.popen(Server_Command_Recive)
			#CmdOutput = CMD.read()
			#client.send(CmdOutput.encode('utf-8'))

		else:
			client.send("\n\n			Server:	Cmd Mode Is Off. Turn it on by typing: CmdOn".encode('utf-8'))

def Start():
	Server()
	ReStart()

def ReStart():
	ListenAndAcceptConnection()
	Listen()


Start()






