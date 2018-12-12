import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50001))
s.listen(5)
print "Communication program about self identity"
data = ''
kamus = {'name':'M. Rifqy Fauzy',
         'NIM':'L200184090',
         'classOf':'2018',
         'quit':'siap!!'}
while data.lower() != 'quit':
    komm, addr = s.accept()
    while data.lower() != 'quit':
        data = komm.recv(1024)
        print 'Command: ',data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("Sorry, the order isn't understood")