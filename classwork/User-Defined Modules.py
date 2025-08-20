# Modules and User-Defined Modules
import operator as opr
a=int(input("Enter a value :"))
b=int(input("Enter b value :"))

op=input("Enter the op(+ - * / % **) :")

if op=='+':
    opr.add(a,b)
elif op=='-':
    opr.sub(a,b)
elif op=='*':
    opr.mul(a,b)
elif op=='/':
    opr.div(a,b)
elif op=='%':
    opr.mod(a,b)
elif op=='**':
    opr.exp(a,b)
else :
    print("Correct opstion")

'''
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def mod(a,b):
    print(a%b)
def exp(a,b):
    print(a**b)
'''

'''
Input :
Enter a value :12
Enter b value :10
Enter the op(+ - * / % **) :*

Ouput :
120
'''



from operator import *
a=int(input("Enter a value :"))
b=int(input("Enter b value :"))

op=input("Enter the op(+ - * / % **) :")

if op=='+':
    add(a,b)
elif op=='-':
    sub(a,b)
elif op=='*':
    mul(a,b)
elif op=='/':
    div(a,b)
elif op=='%':
    mod(a,b)
elif op=='**':
    exp(a,b)
else :
    print("Correct opstion")
    
'''
Input :
Enter a value :10
Enter b value :5
Enter the op(+ - * / % **) :/

Output :
2.0
'''

from operator import add,sub,mul,div,exp,mod
a=int(input("Enter a value :"))
b=int(input("Enter b value :"))

op=input("Enter the op(+ - * / % **) :")

if op=='+':
    add(a,b)
elif op=='-':
    sub(a,b)
elif op=='*':
    mul(a,b)
elif op=='/':
    div(a,b)

elif op=='%':
    mod(a,b)
elif op=='**':
    exp(a,b)

else:
    print("Correct opstion")


'''
Enter a value :10
Enter b value :20
Enter the op(+ - * / % **) :+
30
'''