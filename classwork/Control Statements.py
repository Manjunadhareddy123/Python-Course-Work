# Control Statements

# Table numbers.
num=int(input("Enter the table number :"))# Enter the table number :17
for i in range(1,21):
    print(f"{num} * {i} = {num*i}")
'''
output :
17 * 1 = 17
17 * 2 = 34
17 * 3 = 51
17 * 4 = 68
17 * 5 = 85
17 * 6 = 102
17 * 7 = 119
17 * 8 = 136
17 * 9 = 153
17 * 10 = 170
17 * 11 = 187
17 * 12 = 204
17 * 13 = 221
17 * 14 = 238
17 * 15 = 255
17 * 16 = 272
17 * 17 = 289
17 * 18 = 306
17 * 19 = 323
17 * 20 = 340

'''

# finding the char and it's index

s='Praveen Harhith Varun Sheshu Krishna'.lower()
n=len(s)
ch=input("Enter the char: ").lower() # Enter the char: h
for i in range(n):
    if s[i]==ch:
        print(ch,i)
'''
output :
h 8
h 11
h 14
h 23
h 26
h 33
'''
# products available or not
products=['cycle','watch','laptop','mobile','mouse']
items=input("Enter the items :").split() # Enter the items :cycle watch laptop
for i in items :
    if i in products:
        print(products.index(i),i)
    else :
        print(f"{i} is not available.")
'''       
output
0 cycle
1 watch
2 laptop
'''

# email and password
email,pwd='xyz@gmail.com','xyz@123'
max_attempts=5

while max_attempts>0:
    useremail=input("Enter the email :")
    password=input("Enter the Password :")
    if useremail==email and pwd==password :
        print("Login Successful")
        break
    else :
        print("Invalid Login")
    max_attempts-=1
else :
    print("Try after some time.")

'''
Enter the email :dfq2r
Enter the Password :rw4
Invalid Login
Enter the email :xyz@gmail.com
Enter the Password :xyz@123
Login Successful
'''

# ascii numbers
s='Python Programming'
for ch in s :
    print(ch,ord(ch))
'''
P 80
y 121
t 116
h 104
o 111
n 110
  32
P 80
r 114
o 111
g 103
r 114
a 97
m 109
m 109
i 105
n 110
g 103
'''


# square numbers
s=[1,2,3,4,5,6,7,8,9,0]
for num in s :
    print(num,':',num**2)
'''
1 : 1
2 : 4
3 : 9
4 : 16
5 : 25
6 : 36
7 : 49
8 : 64
9 : 81
0 : 0
'''

# lower to upper
s=("Manju","Kowshik","Koti kiran","Teja")
for name in s :
    print(name.upper())
'''
MANJU
KOWSHIK
KOTI KIRAN
TEJA
'''

# binary numbers
s={1,2,3,4,5,6,7,8,9}
for num in s:
    print(num,':',bin(num))
'''
1 : 0b1
2 : 0b10
3 : 0b11
4 : 0b100
5 : 0b101
6 : 0b110
7 : 0b111
8 : 0b1000
9 : 0b1001
'''


# square numbers
s={1:1,2:4,3:9,4:16,5:25}
for i in s:
    print(i,':',s[i])

'''
1 : 1
2 : 4
3 : 9
4 : 16
5 : 25
'''

#with in range
for i in range(5):
    print(i)
'''
0
1
2
3
4
'''

# odd numbers
for i in range(1,21,2):
    print(i)

'''
1
3
5
7
9
11
13
15
17
19
'''

# even numbers
for i in range(2,21,2):
    print(i)

'''
2
4
6
8
10
12
14
16
18
20
'''

#reverse numbers
for i in range(10,0,-1):
    print(i)

'''
10
9
8
7
6
5
4
3
2
1
'''

#game
bullets=10
while bullets > 0:
    bullets-=1
    print(f"shoot(),{bullets} are left")
print("game over")
'''
shoot(),9 are left
shoot(),8 are left
shoot(),7 are left
shoot(),6 are left
shoot(),5 are left
shoot(),4 are left
shoot(),3 are left
shoot(),2 are left
shoot(),1 are left
shoot(),0 are left
game over
'''


bullets=10
while bullets > 0:
    if bullets>13:
        print("User dead,Game over")
        break
    bullets-=1
    print(f"shoot(),{bullets} are left")
else :
    print("game over.You win the Game")
'''
shoot(),9 are left
shoot(),8 are left
shoot(),7 are left
shoot(),6 are left
shoot(),5 are left
shoot(),4 are left
shoot(),3 are left
shoot(),2 are left
shoot(),1 are left
shoot(),0 are left
game over.You win the Game
'''
