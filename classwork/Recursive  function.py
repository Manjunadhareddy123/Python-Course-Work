# Call by value and call by Refernce

# Int

def update(val):
    val=val+10 # effected by only Inside
    print("Inside Function",val)

val=12
update(val)
print("Outside Function",val)
'''
Output :
Inside Function 22
Outside Function 12
'''

#float

def update(val):
    val=val+10 # effected by only Inside
    print("Inside Function",val)

val=12.6
update(val)
print("Outside Function",val)

'''
Output :
Inside Function 22.6
Outside Function 12.6
'''
# String
def update(val):
    val=val+"  Language" # effected by only Inside
    print("Inside Function : ",val)

val="Python"
update(val)
print("Outside Function : ",val)

'''
Output :
Inside Function :  Python Language
Outside Function :  Python
'''

# List --> effected by both Inside and Outsie
def update(val):
    val.append(7)
    print("Inside Function : ",val)

val=[1,2,3,4,5]
update(val)
print("Outside Function : ",val)
'''
Output :
Inside Function :  [1, 2, 3, 4, 5, 7]
Outside Function :  [1, 2, 3, 4, 5, 7]
'''

# Tuple
def update(val):
    val=val+(2,4) # effected by only Inside.
    print("Inside Function : ",val)

val=(1,2,3,4,5)
update(val)
print("Outside Function : ",val)


'''
Output :
Inside Function :  (1, 2, 3, 4, 5, 2, 4)
Outside Function :  (1, 2, 3, 4, 5)

'''

# Set
def update(val):
    val.add(7) # effected by both Inside and outside
    print("Inside Function : ",val)

val={1,2,3,4,5}
update(val)
print("Outside Function : ",val)

'''
Output :
Inside Function :  {1, 2, 3, 4, 5, 7}
Outside Function :  {1, 2, 3, 4, 5, 7}
'''
# Dict 
def update(val):
    val[6]=36 # effected by both inside and outside
    print("Inside Function : ",val)

val={1:1,2:4,3:9,4:16,5:25}
update(val)
print("Outside Function : ",val)

'''
Output :
Inside Function :  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
Outside Function :  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

'''
# Boolean
def update(val):
    val=True # effected by only Inside.
    print("Inside Function : ",val)

val=False
update(val)
print("Outside Function : ",val)

'''
Output :
Inside Function :  True
Outside Function :  False

'''

#
def update(val):
    val=val.copy() # Shallow copy not effected by Outside.
    val.append(20)
    print("Inside Function : ",val)

val=[1,2,3,4,5]
update(val)
print("Outside Function : ",val)

'''
Output :
Inside Function :  [1, 2, 3, 4, 5, 20]
Outside Function :  [1, 2, 3, 4, 5]
'''


# Recursion
# Syntax.
'''
def add() :
    add()

add()
'''
# Normal 
for i in range(1,11):
    print(i,end=" ")
    
'''
Output :1 2 3 4 5 6 7 8 9 10 
'''
def numbers(n) :
    for i in range(1,n+1):
        print(i,end=" ")

numbers(10)
'''
 Output :1 2 3 4 5 6 7 8 9 10 
'''
# Original Recursion
#10 - 1
def numbers(n) :
    if n==0:
        return
    print(n,end=" ")
    return numbers(n-1)
numbers(10)

'''
Output :10 9 8 7 6 5 4 3 2 1 
'''
# 1-10
def numbers(n) :
    if n==11:
        return
    print(n,end=" ")
    return numbers(n+1)
numbers(1)
'''
Output :1 2 3 4 5 6 7 8 9 10 

'''
# Sum of n
def numbers(n):
    if n==0:
        return n
    print(n,end=" ")
    return n+numbers(n-1)
print("\n",numbers(10))


'''
Output :
10 9 8 7 6 5 4 3 2 1 
 55
'''
def numbers(n):
    if n==0:
        return n
    
    return n+numbers(n-1)
print(numbers(10))
'''
Output :55
'''

# Product
def product(n):
    if n==1:
        return n
    return n*product(n-1)

print(product(10))
''' Output : 3628800 '''

# split()
def display(s,ind):
    if ind==len(s):
        return
    print(s[ind],end=" ")
    display(s,ind+1)
s='Python programming'
display(s,0)
'''
Output :
P y t h o n   p r o g r a m m i n g 
'''

# reverse 
def display(s,ind):
    if ind==-1:
        return
    print(s[ind],end=" ")
    display(s,ind-1)
s='Python programming'
display(s,len(s)-1)
''' 
Output :
g n i m m a r g o r p   n o h t y P 
'''

def display(s,ind):
    if ind==len(s):
        return
    print("Before :",s[ind])
    display(s,ind+1)
    print("After :",s[ind])
s='Python programming'
display(s,0)
'''
Before : P
Before : y
Before : t
Before : h
Before : o
Before : n
Before :
Before : p
Before : r
Before : o
Before : g
Before : r
Before : a
Before : m
Before : m
Before : i
Before : n
Before : g
After : g
After : n
After : i
After : m
After : m
After : a
After : r
After : g
After : o
After : r
After : p
After :
After : n
After : o
After : h
After : t
After : y
After : P

'''

def display(s,ind):
    if ind==len(s):
        return
    print(s[ind],end=" ",)
    display(s,ind+1)
    print(s[ind],end="\t")
s='Python programming'
display(s,0)
'''
P y t h o n   p r o g r a m m i n g 
g   n       i       m       m       a       r       g       o       r       p               n       o       h       t       y       P

'''

# sun of Digits
n=int(input("Enter the Number :"))
while n>0:
    print(n)
    n=n//10
'''
Input :Enter the Number :54765
Output :
54765
5476
547
54
5

'''

n=int(input("Enter the Number :"))
while n>0:
    rem=n%10
    print(n,rem)
    n=n//10
'''
Input :Enter the Number :65465
Output :
65465 5
6546 6
654 4
65 5
6 6

'''
n=int(input("Enter the Number :"))
sum=0
while n>0:
    rem=n%10
    sum+=rem
    #print(n,rem)
    n=n//10
print(sum)
'''
Input :Enter the Number :5435
Output :17
 '''

def sumofdigits(n):
    sumofdigit=0
    while n>0 :
        sumofdigit+=(n%10)
        n=n//10
    return sumofdigit

n=int(input("Enter the Number :"))
print(sumofdigits(n))
'''
Input :Enter the Number :345345
Output :24

'''

def sumofdigits(n):
    if n<=0:
        return 0
    return (n%10)+sumofdigits(n//10)

n=int(input("Enter the Number :"))
print(sumofdigits(n))
'''
Input :Enter the Number :12341234
Output :20

'''


# recursion

# Factorial number
def factorial(n):
    if n==0 or n==1 :
        return 1
    else :
        return n*factorial(n-1)
print(factorial(4))
'''
24
'''
# Fibonacci Series.
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))

# Sum of Natural Numbers
def sumofnum(n):
    if n==1:
        return 1
    else :
        return n+sumofnum(n-1)
print(sumofnum(10))
'''
55
'''