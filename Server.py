from socket import *
port = 1337

listeningSocket = socket(AF_INET, SOCK_STREAM) # create an INET, STREAMing socket
listeningSocket.bind(('', port)) # Ip\Port
listeningSocket.listen(5) # become a server socket
(conn_sock, address) = listeningSocket.accept() # become a server socket

### We assume that str is the message without the header ###
def calculate(str):
    #find the operator
    i = 0
    while str[i]>=0 and str[i]<=9 and i < len(str):
        i+=1
    if i==0 or i>len(str)-1: #ensuring operator isnt first or last object
        raise Exception("Can't lead or end with an operator!")
    
    try:
        num1 = int(str[:i])
        op = str[i]
        num2= int(str[i+1:])
    except:
        raise Exception("Incorrect format, need <int><operator><int>")
    
    ###switch cases now####
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/' :
        return num1 / num2
    else:
        raise Exception("Illegal operator, can only use +, -, /, *")
    
    
def is_palindrome(str):
    try:
        float(str)
    except:
        raise Exception("Input must be a legal int or float!")
    return str == str[::-1]

def is_primary(str):
    try:
        num = int(str)
    except:
        raise Exception("Input must be an integer!")
    
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
