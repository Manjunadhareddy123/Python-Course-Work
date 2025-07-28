#Function Arguments
# 1. Positional Arguments

data=('xyz@gmail.com','xyz@123')
def login (username,mail,password):
    if mail==data[0] and password==data[1] :
        print(f"{username} -Login Successful.")
    else :
        print(f"{username}- Invaild Login")
username=input("Enter the Username :") 
mail=input("Enter the Gmail :")
password=input("Enter the Password :")

login(username,mail,password)

'''
Enter the Username :Manju
Enter the Gmail :xyz@gmail.com
Enter the Password :xyz@123
Manju -Login Successful.

Enter the Username :Manju
Enter the Gmail :xyz@gmail.com
Enter the Password :eeee
Manju- Invaild Login

Enter the Username :Manju
Enter the Gmail :xyz
Enter the Password :xyz@123
Manju- Invaild Login

'''
# 2. Keyword Arguments

data=('xyz@gmail.com','xyz@123')
def login (username,mail,password):
    if mail==data[0] and password==data[1] :
        print(f"{username} -Login Successful.")
    else :
        print(f"{username}- Invaild Login")
usernam=input("Enter the Username :") 
mai=input("Enter the Gmail :")
passwor=input("Enter the Password :")

login(username=usernam,mail=mai,password=passwor)

'''
Enter the Username :Manju
Enter the Gmail :xyz@gmail.com
Enter the Password :xyz@123
Manju -Login Successful.

Enter the Username :Hello
Enter the Gmail :xyz
Enter the Password :xyz@g123
Hello- Invaild Login

'''
# 3. Default Arguments

data=('xyz@gmail.com','xyz@123')
def login (mail,password,username="Hello"):
    if mail==data[0] and password==data[1] :
        print(f"{username} -Login Successful.")
    else :
        print(f"{username}- Invaild Login")
username=input("Enter the Username :") 
mail=input("Enter the Gmail :")
password=input("Enter the Password :")

login(mail,password,username)

'''
Enter the Username :
Enter the Gmail :xyz@gmail.com
Enter the Password :xyz@123
Hello -Login Successful.

Enter the Username :manju
Enter the Gmail :xyz@gmail.com
Enter the Password :xyz@123
Hello -Login Successful.

pra22.py                                                                                      Enter the Username :xyz
Enter the Gmail :xyz@gmail.com
Enter the Password :xyz@123
xyz -Login Successful.

'''

# 4. Variable-Length Arguments
# *args (Arbitrary Positional Arguments)
# Used to pass a variable number of arguments.
def sum(*l):
    for i in l :
        s=s+i
    return s
print(sum(1,2,3,4,5,6,7,8,9,10))
print(sum(3,4,5))
print(sum(1,2))
'''   
55
12
3
'''
# **kwargs (Arbitrary Keyword Arguments)
# Used to pass multiple keyword arguments.
def display(**l):
    return l
print(display(python=34,sql=57,html=50))
print(display(java=54,powerbi=43))
print(display(c=90))
'''
{'python': 34, 'sql': 57, 'html': 50}
{'java': 54, 'powerbi': 43}
{'c': 90}
'''
# Scope of Variables
'''
def outer_fun():
    course="python"

outer_fun()
print(course) # Name Error
'''
def outer_fun():
    course="python"
    print(course)
outer_fun()
'''
 python
'''
'''
def outer_fun():
    course="python"
    print("Inside Function :",course)
outer_fun()
print("Outside Function :",course) # Name Error
'''
# Local
def outer_fun():
    course="python"
    print("Inside Function :",course)
outer_fun()
print("Outside Function :")
'''
Inside Function : python
Outside Function :
'''

def outer_fun():
    
    print("Inside Function :",course)
course="python"
outer_fun()
print("Outside Function :",course)
'''
pra22.py                                                                                      Inside Function : python
Outside Function : python
'''
# Global Scope
def outer_fun():
    global  course
    course="Python"
    print("Inside Function :",course)
outer_fun()
print("Outside Function :",course)
'''
Inside Function : Python
Outside Function : Python
'''


def outer_fun():
    course="python"
    def inner_fun():
        batch=30
        print("Inner Function :",batch,course)
    inner_fun()
    print("Inside Function:",course)
outer_fun()
'''
Inner Function : 30 python
Inside Function: python
'''
'''
def outer_fun():
    course="python"
    def inner_fun():
        batch=30
        print("Inner Function :",batch,course)
    inner_fun()
    print("Inside Function:",course,batch)
outer_fun()                                       # Name Error.
'''
def outer_fun():
    course="python"
    def inner_fun():
        course="Java"
        print("Inner Function :",course)
    inner_fun()
    print("Inside Function:",course)
outer_fun()
'''
Inner Function : Java
Inside Function: python

'''
# 3. Enclosing Scope (Nonlocal Scope)
def outer_fun():
    course="python"
    def inner_fun():
        nonlocal course
        course="Java"
        print("Inner Function :",course)
    inner_fun()
    print("Inside Function:",course)
outer_fun()
'''
Inner Function : Java
Inside Function: Java
'''

# 4. Built-in Scope
l=[1,2,3,4,5]
print(l)
'''
[1, 2, 3, 4, 5]
'''
l=[1,2,3,4,5]
print(sum(l))
'''
15
'''

'''
l=[1,2,3,4,5]
sum=0
print(sum(l)) # Type Error.
'''

def add(a,b) :
    return a+b
print(add(2,3)) # 5



'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
exp=input("enter the experssion:")
op=None
for i in exp:
    if not i.isdigit():
        op=i
        break
a,b=exp.split(op)
a,b=int(a),int(b)
if op=='+':
    print(add(a,b))
elif op=='-':
    print(sub(a,b))
elif op=='*':
    print(mul(a,b))
elif op=='/':
    print(div(a,b))
elif op=='%':
    print(mod(a,b))
'''