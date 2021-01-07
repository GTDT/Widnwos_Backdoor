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
  |		   .----.   .--.   .---. .-. .-..----.  .----.  .----. .----.			|
  |		   | {}  } / {} \ /  ___}| |/ / | {}  \/  {}  \/  {}  \| {}  }			|
  |		   | {}  }/  /\  \\     }| |\ \ |     /\      /\      /| .-. \			|
  |		   `----' `-'  `-' `---' `-' `-'`----'  `----'  `----' `-' `-'			|
  |_____________________________________________________________________________________________|

"""



import socket, os, subprocess

Shutdown_The_Server_Confirmation_Message = """
		You closed server script!!

"""

def connect():
	Host, Port = 'localhost', 6482
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def ConnToTheServer():
		try:
			client.connect((Host, Port))
		except:
			ConnToTheServer()

	ConnToTheServer()
	print(client.recv(2048).decode('utf-8'))

	while True:
		command_input = input(f"{Host, Port}: >> ")
		client.send(command_input.encode('utf-8'))
		print(client.recv(1024).decode('utf-8'))

		if SCR == "DISCONNECT" or SCR == "Disconnect" or SCR == "disconnect":
			exit()

		if command_input == "Exit_Confirm_True":
			os.system('cls' if os.name == 'nt' else 'clear')
			print(client.recv(1024).decode('utf-8'))
			exit()

connect()




