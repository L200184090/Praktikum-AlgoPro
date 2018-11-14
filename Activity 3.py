Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ##Practical 6, Activity 3, Muhammad Rifqy Fauzy, L200184090
>>> Name = 'Muhammad Rifqy Fauzy'
>>> ##This command put a string 'Muhammad Rifqy Fauzy' into the Name data as value
>>> Name
'Muhammad Rifqy Fauzy'
>>> NIM = 'L200184090'
>>> ##This command put a string 'L200184090' into the NIM data as a value
>>> NIM
'L200184090'
>>> X = '1' + NIM[7:]
>>> ##This command add a slice of NIM data (from the 7th character until the end of the string) to '1' string, and define them as X data
>>> X
'1090'
>>> a = int(X)
>>> ##This command convert the value of X data (string) into a integer type, and define them as the value of a
>>> a
1090
>>> b = len(Name)
>>> ##This command calculate the length of the string in Name data (integer), and define them as the value of b.
b
>>> 
>>> b
20
>>> type(a)
<class 'int'>
>>> ##Python give that response because the data type of a is an integer
>>> type(b)
<class 'int'>
>>> ##Python give that response because the type of b data is an integer
>>> a/b
54.5
>>> ##this command make Python operate the value of a, divide it by the value of b
>>> a//b
54
>>> ##this command also divide the value of a by the value of b, but the result will be an integer, and the value of a/b is a float
>>> 10 * (a-999)
910
>>> ##this command subtract the value of a by 999 and then multiply it by 10
>>> b**2
400
>>> ##this command operate the value of b. The operation is b^2 (b power 2 -- multiply the value of b by itself)
>>> a%b
10
>>> ##This command give result after dividing the value of a and b, and count the divide remainder.
>>> 
>>> c = 12.5
>>> ##this command put a value 12.5 into the variable of c
>>> c
12.5
>>> type(c)
<class 'float'>
>>> ##Python give that response because the data type of c is float (decimal number).
>>> a/c
87.2
>>> ##this command divide the value of a by the value of c (if an integer divided by float, the result is float).
>>> a//c
87.0
>>> ##this command also divide the value of a by the value of c, but the result will be integrated (to an integer)
>>> a%c
2.5
>>> ##This command give result after dividing the value of a by c, and count the divide remainder.
>>> c > b
False
>>> ##The result is 'False' because the value of b is greater than c
>>> type(c > b)
<class 'bool'>
>>> ##bool (boolean) is a data type that determine something is true or false
>>> a > b and b > c
True
>>> ##Python give that response because the value of a is greater than b (true) and the value of b is greater than c (true)
>>> ##note: the result will be true if and only if the 2 booleans has 'True' result, if hey are connected by 'and'
>>> a > 1100 or b < 10
False
>>> ##Python give that response because the 2 booleans have the 'False' value, 1100 is greater than the value of a, and the value of b is greater than 10.
>>> ##note: if 2 boolean connected by 'or', the resolt will be 'True' although only one boolean have the result 'True'
>>> 
