#make a chatting program using socket (소켓을 이용한 채팅프로그램 만들기)
#made by burning sweetpotato


import socket

"""before the connect, I made a print statement,
enter a nickname to feeling of the chatting room"""


print("welcome self chatting program")
name = raw_input("Before the start, please enter your nickname: ")
print("Hi" + name + " !! nice to meet you. Let's start connect!")


if name:
    """this made for connect server using socket."""
    """ setup the hostand prot"""
    
    HOST = '127.0.0.1'  """Can access localhost"""
    PORT = 50000
    addr = (HOST,PORT)

    """make s for call AF_INET(the place for server and client),
        SOCK_STREAM(type of socke)"""
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr) """connect HOST and PROT"""
    s.send(name)   """send to data and recive"""
    data = s.recv(1024)

    """this made for message, after passed to the sever. if I enter the message (raw_input()),
       that was passed to sever by send() and receive back recv() """
    
    while 1:
        print("connect complete!")
        message = raw_input("enter youre sentence: ")
        mes = bytes(message)
        s.send(mes)
        data = s.recv(1024)     


    """if done, we have to close socket"""           
    s.close()
