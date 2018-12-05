#-----------------------Practical 9-----------------------#
##Activity 1

g = open("Activity 1.txt","w")
g.write('L200184090'+'\n'+'04-08-2000'+'\n'+'Muhammad Rifqy Fauzy')
g.close()



##Activity 2

f = open("Activity 1.txt", "r")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
line4 = "Bengkulu"
f.close()

h = open("Activity 1.txt", "w")
h.write(line1 + line2[3:5] + '-' + line2[0:2] + line2[5:] + line3 + "\n" + line4)
h.close()



##Activity 3

import shelve

d = open("Activity 1.txt", "r")
line1 = d.readline()
line2 = d.readline()
line3 = d.readline()
line4 = d.readline()
d.close()

F = shelve.open("Activity 1.data")
F["baris1"] = line1
F["baris2"] = line2
F["baris3"] = line3
F["baris4"] = line4
F.close()



##Activity 4

X = shelve.open("Activity 1.data")
print("Nama: ", X["baris3"][0:-1])
print("NIM: ", X["baris1"][0:-1])
print("Tempat Lahir: ", X["baris4"])
print("Tanggal Lahir: ", X["baris2"])
print(X["baris3"][9:14])
X.close()