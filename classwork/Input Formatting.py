# Input Formatting


# 1. String Input
name=input("Enter the name : ")
# Enter the name : java
print(name) # java
print(type(name))# <class 'str'>

"python program lanuage".split() # ['python', 'program', 'lanuage']
item_1=input("Enter The items_1 : ") # Enter The items_1 : coffe tea pizza
print(item_1) # coffe tea pizza
print(type(item_1)) # <class 'str'>

item_2=input("Enter The items_2 : ") # Enter The items_2 : 1 2 3 4 5
print(item_2) # 1 2 3 4 5
print(type(item_2)) # <class 'str'>
item_2 # '1 2 3 4 5'

price=input("Enter the price")
# Enter the price 245.55
print(price) # 245.55

price=input("Enter the price")
# Enter the price230
print(price) # 230
print(type(price))#<class 'str'>

# 2. Integer Input
price1=int(input("Enter the price"))
# Enter the price 234
print(price1) # 234
print(type(price1)) # <class 'int'>

# 3. Float Input
dis=float(input("Enter the discount : "))
# Enter the discount : 234.55
print(type(dis)) # <class 'float'>
print(dis) # 234.55

# map
item_3=map(int,input("Enter the input : "))# Enter the input : 5 6 7 8
item_3 # <map object at 0x000001E575DB9FF0>
print(item_3) # <map object at 0x000001E575DB9FF0>
print(type(item_3)) # <class 'map'>

# List
#  Input as List (Space-separated)
l3=input("Enter student names (space-separated) : ").split()
# Enter student names (space-separated) : manju nadha reddy
print("students names : ",l3) # students names :  ['manju', 'nadha', 'reddy']
print(type(l3)) # 
<class 'list'>

# Input as List (Comma-separated)
l4=input("Enter emp names (Comma-separated) : ").split(',')
# Enter emp names (Comma-separated) : kowshik,teja,kiran
print("emp names : ",l4) # emp names :  ['kowshik', 'teja', 'kiran']
print(type(l4)) # <class 'list'>

# List of Integers
m3=list(map(int, input("Enter the m3 input : ").split()))
# Enter the m3 input : 4 3 5 6
print(m3) #  [4, 3, 5, 6]
print(type(m3)) # <class 'list'>

# List of Floats
f3=list(map(float, input("Enter the weights : ").split()))
# Enter the weights : 55.6 22.7
print("weights : ",f3) # weights :  [55.6, 22.7]
print(type(f3)) # <class 'list'>

# Tuple Input
m4=tuple(map(int,input("Enter the m4 values : ").split()))
# Enter the m4 values : 6 7 8 9 10
print(m4) # (6, 7, 8, 9, 10)
print(type(m4)) # <class 'tuple'>


# Set Input
m5=set(map(int,input("Enter the m5 values : ").split()))
# Enter the m5 values : 1 3 5 6 8
print("m5 values",m5) # m5 values {1, 3, 5, 6, 8}

# Dictionary Input using eval()
m6=eval(input("Enter dict values : "))
# Enter dict values : {1:2,3:4,5:6}
print("m6 dict values : ",m6) # m6 dict values :  {1: 2, 3: 4, 5: 6}
print(type(m6))# <class 'dict'>

#  Multiple Inputs with Unpacking -->Use case: Login form or payment details.

a,b=input("Enter  the two values : ").split()
Enter  the two values : 4 5.6
print("a value : ",a)
a value :  4
print("b value : ",b)
b value :  5.6



