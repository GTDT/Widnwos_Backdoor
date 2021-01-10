## Importing os module.
import os


def ClearWindow():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""\n

	█████████████████████████████████████████████████████████████████████████████████
	█══╗░░░░║░░░░╔════╦╗░░░░░║░░░░░░░░░░░░░░░░░░░░░░░░░░░░║░░╔═░░░░══╗░░║░░░░░║░░║░░█
	█░░╚╦═╦═╩╗░░░╠═░░░║╚╦══░╔╣░░░░╔═══╦════╦═══╦════╗░░░░░╚═╦╝░░░░░░░╠══╬╗░░░░║░░║░░█
	█═╦═╝░╚══╬═╦═╝║░╔═╩╦╝░░═╬╩═░░░║╔═╗║╔╗╔╗╠╗╔╗║╔╗╔╗║░░░░░░░╚═══╗░═╗░║░░║╚══╦╦╩╗╔╩══█
	█░╚╦══╗░░║═╝║░╠═╝╔═╩╦╦══╝░░░░░║║░╚╩╝║║╚╝║║║╠╝║║╚╝░░░░░═╗░░░░╚══╚╦══╦╬╗░░║╚╗╚╩╗░░█
	█░░╚═╗╚═╗╚╗░╚╗║╔╦╝░░║╚╗░░╔═░░░║║╔═╗░║║░░║║║║░║║░░░░░░░░╚═╗░░░░░╔╝░╔╝║╚╗╔═░╠═░╚╗░█
	█░░║░╚══╬═╬═░╚╬╩╝░░╔╝░╚╗╔╝░░░░║╚╩═║░║║░╔╝╚╝║░║║░░░░░░═╗░░╚═╦╗░╔╣░╔╣░║░╚╣░═╩╗░░║░█
	█░╔╩╗░╔═╣░╠═╗░║░╔══╩═░╔╩╝░░░░░╚═══╝░╚╝░╚═══╝░╚╝░░░░░░░╚╗░░╔╣╚╗║╚╗║║░║░░╠╗░░╚╗░║░█
	█═╝╔╩═╝╔╝░║░╚═╠═╝░░░╔═╝░░░╔══╗░░░░░░╔╗░╔═══╗░░░░░░░░░░░╠══╝╚╗╚══╚═╬═╬╗╔╝╠╦╗░║░║░█
	█░░║░░╔╝░═╩╗░╔╣░║║░░╠═░░░░║╔╗║░░░░░░║║░╚╗╔╗║░░░░░░░░░░░║░░░░║░░╔═╦╝░╠╬╣░║║╚═╬═══█
	█░╔╝╔╦╝░║░░║╔╝╠═╝║╔╦╝░╔═░░║╚╝╚╦══╦══╣║╔╗║║║╠══╦══╦═╗░░╔╝░░║░╚╦═╝░╚╦═║╚╬═░║░░╚╗░░█
	█═╩╦╝║╔═╩╦═╣║░║░╔╩╝╚═╦╝░░░║╔═╗║╔╗║╔═╣╚╝╝║║║║╔╗║╔╗║╔╝░░╠═╗░╚═╗╚╗░╔═╝░║░╠═░╚╦╦═╩╗░█
	█░╔╝░═╬═░║░╚═╗║╔╣░╔═░║░║░░║╚═╝║╔╗║╚═╣╔╗╦╝╚╝║╚╝║╚╝║║░░░║░║░░░╚╗║░║░╔═║░╚╗░═╝╚╗░║░█
	█╔╣░░═╣░░║░░░╚╬╝╚═╣░░╠═╝░░╚═══╩╝╚╩══╩╝╚╩═══╩══╩══╩╝░░░░╔═══╦═╩════╩═╬══╣░╔══╩═╣░█
	█║╚══░║░░║░░░░║░░░╚═░║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░═╝░░░║░░░░░░░░║░░║░║░░░░║░█
	█████████████████████████████████████████████████████████████████████████████████

	\n""")

ClearWindow()

## Importing socket module.
import socket, time

## The name explains it self
Shutdown_The_Server_Confirmation_Message = """
		You just closed server script!!

"""

## Definition/Function that starts all the script.
def Start():
	Host, Port = 'localhost', 6482
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(120)
	print("				  Waiting for server to respond...")

	## Definition/Function that tries to connects to the server.
	def ConnToTheServer():
		try:
			client.connect((Host, Port))
		except:
			ConnToTheServer()

	ConnToTheServer()
	print(client.recv(2048).decode('utf-8'))

	## While loop for user input, message recive, command sending and local commands.
	while True:
		command_input = input(f"\n  {Host, Port}: >> ")
		client.send(command_input.encode('utf-8'))
		print(client.recv(2048).decode('utf-8'))

		if command_input == "DISCONNECT" or command_input == "Disconnect" or command_input == "disconnect":
			exit()

		if command_input == "Server_Shutdown_Confirm":
			os.system('cls' if os.name == 'nt' else 'clear')
			time.sleep(0.2)
			print(client.recv(2048).decode('utf-8'))
			exit()

		if command_input == "Cls" or command_input == "cls":
			ClearWindow()

Start()




