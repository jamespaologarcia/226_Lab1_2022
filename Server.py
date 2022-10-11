import socket
BUF_SIZE = 1024
HOST = ''
PORT = 12345
board =  [[['_' for _ in range(4)]  for _ in range(4)] for _ in range(4)]
count = 0
#Function to add entry to the board
def insertToBoard(userInput): 
	global count
	try:
		posOne = int(userInput[3])
		posTwo = int(userInput[4])
		posThree = int(userInput[5])
		inputValue = userInput[6]
		if posOne > 3:
			result = 'E\n'
		elif posTwo > 3:
			result = 'E\n'
		elif posThree > 3:
			result = 'E\n'
		else:
			if board[posOne][posTwo][posThree] == '_':
				if int(inputValue) - 1 == int(count) :
					board[posOne][posTwo][posThree] = inputValue
					result = 'O\n'
					count = int(count) + 1
					if int(count) == 3 :
							count = 0
				else :
					result = 'E\n'
			else:
					result = 'E\n'
	except:
		result = 'E\n'
	return result
#Function to display the board
def showBoard(result):
	global board
	for row in board :
		if result != '':
			result = result + '\n'
		for ro in row :
			result = result + '\n'
			for r in ro :
				result = result + r	
	return result
#Function to clear the board
def clearBoard():
	global board 
	board = [[['_' for _ in range(4)]  for _ in range(4)] for _ in range(4)]
	global count
	count = 0
	return 'O\n'
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
			result = ''
			if action == 'P':
				result = insertToBoard(userInput)
			elif action == 'C' :
				result = clearBoard()
			elif action == 'G':
				result = showBoard(result)
				result = result.split('\n', 1)[1] + '\n\n\n'
			else:
				result = str('E\n')
			sc.sendall(result.encode())
