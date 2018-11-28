##Activity 1

b = '''Pilihan yang tersedia:
b menampilkan bantuan ini
N menampilkan NIM
a menampilkan Nama
A menampilkan Alamat
x menampilkan Tempat Lahir
s menampilkan Status/pekerjaan
p menampilkan Program Studi
f menampilkan Fakultas
k keluar'''
print(b)
print(' ')
D = {'N':'NIM: L200184090','a':'Nama: Muhammad Rifqy Fauzy','A':'Alamat: Gonilan','s':'Status/pekerjaan: Mahasiswa','p':'Prodi: Informatika','f':'Fakultas: Fakultas Komunikasi dan Informatika','x':'Tempat Lahir: Bengkulu'}
print(' ')
p = input('Pilihan Saudara: ')
while p != 'k':
    if p in D.keys():
        print(D[p])
        print(' ')
    elif p == 'b':
        print(b)
        print(' ')
    else:
        print('Maaf,', p, 'tidak termasuk dalam pilihan yang tersedia')
        print(' ')
    p = input('Pilihan Saudara: ')
print('Terima Kasih')



#Activity 2

def konversiSuhu(x):
    if x[0] == 'C':
        print('Suhu',x[4:],'Celcius setara dengan',int(((int(x[4:])/5)*9)+32),'Farenheit')
    elif x[0] == 'F':
        print('Suhu',x[4:], 'Farenheit setara dengan',int((int(x[4:])-32)/9)*5, 'Celcius')
    else:
        print('Fungsi ini hanya mengkonversi Celcius ke Farenheit atau sebaliknya')
        
#jangan lupa gunakan tanda petik (') saat menulis argument dalam tanda kurung;contoh: konversiSuhu('C = 40')