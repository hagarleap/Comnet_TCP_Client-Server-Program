from socket import *
ip = 'localhost' # '127.0.0.1'
port = 1337

clientSoc = socket(AF_INET, SOCK_STREAM) # create an INET, STREAMing socket
clientSoc.connect((ip, port))