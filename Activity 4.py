Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ##Practical 6, Activity 4, Muhammad Rifqy Fauzy, L200184090
>>> Name = 'Muhammad Rifqy Fauzy'
>>> ##This command put a string 'Muhammad Rifqy Fauzy' into the Name variable as value
>>> NIM = 190 ##the actual three last digits of the NIM is 090
>>> ##This command put a number 190 (integer) as a value of NIM variable
>>> Height = 1.60
>>> ##This command put a number 1.60 (float) as a value of Height variable
>>> Weight = 61
>>> ##This command put a number 61 (integer) as a value of Weight variable
>>> BirthYear = 2000
>>> ##This command put a number 2000 (integer) as a value of BirthYear variable
>>> Aku = (BirthYear, Weight, Height, NIM, Name)
>>> ##This command make a new tuple named 'Aku' and put some data into the tuple
>>> Data = [BirthYear, Weight, Height, NIM, Name]
>>> ##This command make a new list named 'Data' and put some data into the list
>>> 
>>> type(Aku)
<class 'tuple'>
>>> ##Tuple is a group of data that is non-mutable, can't be edited.
>>> Aku[0]
2000
>>> ##This command return the value of the first data in the 'Aku' tuple
>>> a = NIM % 4; Aku[a]
1.6
>>> ##The value of NIM % 4 is 2. The command 'Aku[a]' is to looking for a data in the Aku variable with index a. a equal 2. And the data in the Aku variable with index 2 is 1.6 (Weight)
>>> type(Aku[a])
<class 'float'>
>>> ##The data with index a in the Aku variable is 1.6. If a number is decimal, the type is float
>>> Aku[a:4]
(1.6, 190)
>>> ##This command slice some data in the Aku variable from index a (which is 2) to index 4. but the data with index 4 will not be included
>>> type(Aku[4])
<class 'str'>
>>> ##the data in Aku variable with index 4 is 'Muhammad Rifqy Fauzy', which is a string type of data
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> ##Python give an error response because the data in a tuple is can't be modified / mutated
>>> 
>>> type(Data)
<class 'list'>
>>> ##List is a group of datas that still can be mutated / modified
>>> type(Data[4])
<class 'str'>
>>> ##The data with index 4 in the 'Data' variable is 'Muhammad Rifqy Fauzy', which is a string type of data
>>> Data[4][5]
'm'
>>> ##This command slices the 5th character from the data with index 4 ('Muhammad Rifqy Fauzy'). The 5th letter from the string is 'm'
>>> Data[4][a:6]
'hamm'
>>> ##This command also give a slice of the string 'Muhammad Rifqy Fauzy'. The slice is from the 4th to the 6th letter from the string, but the 6th letter will not be included
>>> Data[0] = 'ok'; Data
['ok', 61, 1.6, 190, 'Muhammad Rifqy Fauzy']
>>> ##This command change / modify the data with index 0 from the 'Data' variable (the first data from the variable) from the number 2000 into a string 'ok'
>>> Data[-a]
190
>>> ##This command slice the data with the index -a (a equal to 2, so the slice is index -2, the second from the last data) which is the number 190
>>> range(a)
range(0, 2)
>>> ##a is equal to 2. The commmand used to make a range from 0 to 2 (to the value of a, if and only if the value of a is an integer)
>>> 
