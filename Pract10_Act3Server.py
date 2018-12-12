import socket

def persegi(s=0):
    return s*s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50020))
s.listen(5)
print "Automatic answer server is ready"
data = ''
while data.lower() != 'quit':
    komm, addr = s.accept()
    while data.lower() !='quit':
        data = komm.recv(1024)
        print 'Message:', data
        if data.find("parameter")!= -1:
            param,value= data.split("=")
            if param == "side parameter":
                s = float(value)
                b = value
                komm.send("parameter recorded")
        elif data == 'calculate':
            komm.send('area of the square with side {} is {}'.format (b,persegi(s)))
        else:
            komm.send('nothing')