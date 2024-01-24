from socket import *
port = 1337

listeningSocket = socket(AF_INET, SOCK_STREAM) # create an INET, STREAMing socket
listeningSocket.bind(('', port)) # Ip\Port
listeningSocket.listen(5) # become a server socket
(conn_sock, address) = listeningSocket.accept() # become a server socket




### packet decoding, assumes packet is full message and not partial###
def login_parser(user_packet, password_packet):
    
    if user_packet[:6] == "User: ":
        username = user_packet[6:]
    else:
        raise Exception("Send username in correct format")
    
    if password_packet[:10] == "Password: ":
        password = user_packet[10:]
    else:
        raise Exception("Send password in correct format")
    
    return login_checker(username, password)

### compares input password and username, assumes file is open ###    
def login_checker(username, password, pass_file):
    pass_file.seek(0) #restart from the top
    for line in pass_file:
        if line[:len(username)] == username:
            if line[len(username)+1 : -1] == password: #ignores newline, username and the separating tab
                return True
    return False        
        

# def function_parser(packet):
#     ### switch cases for header ##
#     try:
#         if packet[:11] == "calculate: ":
#             response = calculate(packet[11:])
#         elif packet[:15] == "is_palindrome: ":
#             response = is_palindrome(packet[15:])
#         elif packet[:12] == "is_primary: ":
#             response = is_primary(packet[12:])
#         else:
#             raise Exception("Send password in correct format")
#     except:
        
#     return f"response: {response}"
    

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
            return "No"
    return "Yes"
