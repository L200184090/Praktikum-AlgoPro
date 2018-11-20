##=========================Chapter 7==============================##



##1st activity

##A = {}
##A['Triangle'] = '0.5 * a * t'
##A['Square'] = 's**2'
##A['Rectangle'] = 'p * l'
##A['Circle'] = 'pi * r**2'
##A['Parallelogram'] = 'a * t'
##
##print('''
##No  |  Nama bangun     |  Rumus luas
##----|------------------|------------------
##1   |  Triangle        | ''',A['Triangle'],'''
##2   |  Square          | ''',A['Square'],'''
##3   |  Rectangle       | ''',A['Rectangle'],'''
##4   |  Circle          | ''',A['Circle'],'''
##5   |  Parallelogram   | ''',A['Parallelogram'])



#2nd activity

##pw = 'AP2018'
##p = input('Masukkan password:  ')
##i = 0
##if p == pw:
##    print('Anda berhasil login')
##else:
##    while i <= 1:
##        p = input('Maaf, anda salah memasukkan password. Masukkan password:  ')
##        i = i + 1
##    print('Anda telah mencoba 3 kali. Akses anda ditolak')



#3rd activity

##t = ('Pagi','Siang','Sore','Petang','Malam')
##p = input('Masukkan nama saudara:  ')
##q = input('Pukul berapa sekarang?  ')
##if q[0] == '0':
##    print('Selamat',t[0],p+'!')
##elif int(q[0:2]) in range(10,12):
##    print('Selamat',t[0],p+'!')
##elif int(q[0:2]) in range(12,15):
##    print('Selamat',t[1],p+'!')
##elif int(q[0:2]) in range(15,18):
##    print('Selamat',t[2],p+'!')
##elif int(q[0:2]) in range(18,20):
##    print('Selamat',t[3],p+'!')
##else:
##    print('Selamat',t[4],p+'!')