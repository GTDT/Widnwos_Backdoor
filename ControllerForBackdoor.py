## Importing os module.
import os

os.system('cls' if os.name == 'nt' else 'clear')

print("""\n

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

\n""")



## Importing socket module.
import socket

## The name explains it self
Shutdown_The_Server_Confirmation_Message = """
		You just closed server script!!

"""

## Definition/Function that starts all the script.
def Start():
	Host, Port = 'localhost', 6482
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(120)
	print("		   waiting for server responce...")

	## Definition/Function that tries to connects to the server.
	def ConnToTheServer():
		try:
			client.connect((Host, Port))
		except:
			ConnToTheServer()

	ConnToTheServer()
	print(client.recv(2048).decode('utf-8'))

	## While loop for user input, message recive, command sending and some local commands.
	while True:
		command_input = input(f"\n  {Host, Port}: >> ")
		client.send(command_input.encode('utf-8'))
		print(client.recv(1024).decode('utf-8'))

		if SCR == "DISCONNECT" or SCR == "Disconnect" or SCR == "disconnect":
			exit()

		if command_input == "Exit_Confirm_True":
			os.system('cls' if os.name == 'nt' else 'clear')
			print(client.recv(1024).decode('utf-8'))
			exit()

Start()




