import socket
BUF_SIZE = 1024
HOST = ''
PORT = 12345
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # TCP socket
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Details later
	sock.bind((HOST, PORT)) # Claim messages sent to port "PORT"
	sock.listen(1) # Enable server to receive 1 connection at a time
	print('Server:', sock.getsockname()) # Source IP and port
	while True:
		sc, sockname = sock.accept() # Wait until a connection is established
		with sc:
			print('Client:', sc.getpeername()) # Dest. IP and port
			message = 'Received '
			newLine = '\n'
			data = message.encode() + sc.recv(BUF_SIZE) + newLine.encode() # recvfrom not needed since address is known
			print(data)
			sc.sendall(data) # Dest. IP and port implicit due to accept call
