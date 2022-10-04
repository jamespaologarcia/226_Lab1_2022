import socket
BUF_SIZE = 1024
HOST = ''
PORT = 12345
board =  [[['-' for _ in range(4)]  for _ in range(4)] for _ in range(4)]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # TCP socket
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Details later
	sock.bind((HOST, PORT)) # Claim messages sent to port "PORT"
	sock.listen(1) # Enable server to receive 1 connection at a time
	print('Server:', sock.getsockname()) # Source IP and port
	while True:
		sc, sockname = sock.accept() # Wait until a connection is established
		with sc:
			print('Client:', sc.getpeername()) # Dest. IP and port
			data = sc.recv(BUF_SIZE) # recvfrom not needed since address is known
			userInput = list(str(data))
			action = userInput[2]
			errorMessage = ''
			if action == 'P':
				posOne = int(userInput[3])
				posTwo = int(userInput[4])
				posThree = int(userInput[5])
				if posOne > 3:
					errorMessage = errorMessage + 'First position is out of range \n' + data + '\n'
				if posTwo > 3:
					errorMessage = errorMessage + 'Second position is out of range \n'
				if posThree > 3:
					errorMessage = errorMessage + 'Third position is out of range \n'
				if errorMessage != '':
					sc.sendall(errorMessage.encode())
				else:
					inputValue = userInput[6]
					if board[posOne][posTwo][posThree] == '-':
						board[posOne][posTwo][posThree] = inputValue
						result = 'OK \n'
						sc.sendall(result.encode())
					else:
						result = 'ERROR \n'
						sc.sendall(result.encode())
			elif action == 'G':
				result = ''
				for row in board :
					result = result + '\n'
					for ro in row :
						result = result + '\n'
						for r in ro :
							result = result + r
				result = result + '\n'
				sc.sendall(result.encode())
			else:
				result = 0
				sc.sendall(result.encode())
