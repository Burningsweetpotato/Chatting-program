#make a chatting program using socket (소켓을 이용한 채팅프로그램 만들기)
#made by burning sweetpotato
#This accept just one client(monology program)


import socket
"""using the socket, make a one server"""
"""make s for call AF_INET(the place for server and client),
        SOCK_STREAM(type of socke)"""

HOST = ''
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))
"""Function bind() allow the server socket 's' start server by
    The HOST(sever-side socket)and PORT(port number)"""
    
s.listen(1)

conn,addr = s.accept() """function for accept client signal"""
print('connected by',addr) """check for access server"""

name = conn.recv(10)
"""recevied client's sentence. so name is nickname in client"""

data = '***'+name+' is log in now'
print(data)


 """this is for chatting using send(), recv()"""
while data:
    conn.send(data)
    data = name+' :  ' + conn.recv(1024)
    print(data)
   
   
conn.close()    
    
      
