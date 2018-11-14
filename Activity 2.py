import random
Name = 'Muhammad Rifqy Fauzy'
DateOfBirth = '04 August 2000'
ShortName = Name[0] + '. ' + Name[9] + '. ' + Name[-5:]
Username = Name[0] + DateOfBirth[0:2] + DateOfBirth[-4:]
Password = Name[0:3] + str(random.randint(100,1000))