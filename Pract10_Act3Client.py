import socket

hostname = 'localhost'
message = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50020))
print "Calculate the area of a square"
while message != 'quit':
    message = raw_input('message :  ')
    s.send(message)
    if message.lower() == 'quit':
        response = s.recv(1024)
        print 'respon: -'
        s.close()
        break
    elif message.lower() != 'quit':
        response = s.recv(1024)
        print 'respon:', response
s.close()