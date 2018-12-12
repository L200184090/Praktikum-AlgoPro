import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,50001))
print "Communication program about self identity"

while pesan.lower() != 'q':
    pesan = raw_input('Command: ')
    s.send(pesan)
    if pesan.lower() == 'quit':
        response = s.recv(1024)
        print 'Jawab:', response
        s.close()
        break
    elif pesan.lower() != 'quit':
        response = s.recv(1024)
        print 'Response:', response
s.close()