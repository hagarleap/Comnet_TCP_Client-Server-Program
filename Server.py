from socket import *
port = 1337

listeningSocket = socket(AF_INET, SOCK_STREAM) # create an INET, STREAMing socket
listeningSocket.bind(('', port)) # Ip\Port
listeningSocket.listen(5) # become a server socket
(conn_sock, address) = listeningSocket.accept() # become a server socket
