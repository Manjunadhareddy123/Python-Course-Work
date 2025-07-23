# Control Statements


# FOR LOOP
work=[1,1,1,0,1,1,0]
current=0
longer=0
for day in work :
    if day==1 :
        current +=1
        if current > longer :
            longer=current
    else :
        current=0
print("longest_streak",longer) 

'''
longest_streak 3
'''

# WHILE LOOP
current="12345"
attempts=0
max_attempts=3
while attempts < max_attempts :
    enter_attempts=input("Enter the PIN : ")
    if enter_attempts == current :
        print("Login Successful.")
        break
    else :
        print("Sorry ,Try another Time.")
        attempts +=1
else :
    print("Your Attempts are finished,try for some time aftetr.")

'''
Enter the PIN : 1111
Sorry ,Try another Time.
Enter the PIN : 11111
Sorry ,Try another Time.
Enter the PIN : 12345
Login Successful.
'''



# FOR LOOP WITH ELSE
notifications=[0,0,0,0]
for notification in notifications :
    if notification==1:
        print("You have unread notifications!.")
        break
else :
    print("All caught up!.")
'''
All caught up!.
'''


# WHILE LOOP WITH ELSE
correct_opt="1231"
current_attempts=0
max_attempts=3
while current_attempts < max_attempts :
    enter_attempt=input("Enter the Opt :")
    if enter_attempt == correct_opt :
        print("Opt successfully.")
        break
    else :
        print("Opt is incorrect.")
        current_attempts +=1
else :
    print("OTP expired.Request a new one.")

'''
ra22.py                                                                                        Enter the Opt :1233
Opt is incorrect.
Enter the Opt :12
Opt is incorrect.
Enter the Opt :1231
Opt successfully.
'''


# break Statement in Python
numbers=[1,2,3,4,5,6,7,8]
target=7
for num in numbers :
    if num == target :
        print("Target found : ",num)
        break

'''
Target found :  7
'''


# continue Statement in Python
for num in range(1,10) :
    if num % 2==0 :
        continue
    print(num,end=" ")

'''
1 3 5 7 9 
'''

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
