# 1. Add Two Numbers
def add(a,b):
    return a+b
a,b=(input("Enter the a Value :").split())
a,b=int(a),int(b)
print("The Sum is :",add(a,b))
'''
Enter the a Value :10 5
The Sum is : 15
'''

# 2. Square a Number
def square(n):
    return n**2
n=int(input("Enter a number : "))
print("The Square is :",square(n))
'''
Enter a number : 4
The Square is : 16
'''
#3. Area of a Circle
def area(n):
    return 3.14*(n**2) #A = π r²
n=int(input("Enter Radius :"))
print(area(n))
'''
Enter Radius :3
28.26
'''
# 4. Greet the User
def greet(name):
    return name
name=input("Enter your name :")
print("Hello,",greet(name))
'''
Enter your name :Alice
Hello, Alice
'''

# 5. Convert Celsius to Fahrenheit
def temp(celsius):
    return (celsius*9/5)+32 # (37°C × 9/5) + 32 = 98.6°F

celsius=int(input("Enter temperature in Celsius :" )) 
print("Temperature in Fahrenheit:",temp(celsius))
'''
Enter temperature in Celsius :36
Temperature in Fahrenheit: 96.8
'''

# 6. Multiply Three Numbers
def multi(a,b,c) :
    return a*b*c

a,b,c=input("Enter the Three numbers :").split()
a,b,c=int(a),int(b),int(c)

print("product is:",multi(a,b,c))
'''
Enter the Three numbers :2 3 4
product is: 24
'''
# 7. Calculate Simple Interest
def simple_interest(a,t,r):
    return (a*t*r)/100

a,t,r=input("Enter Principal, Rate and Time :").split()
a,t,r=int(a),int(t),int(r)

print(simple_interest(a,t,r))
'''
Enter Principal, Rate and Time :1000 5 2
100.0
'''

# 8. Find Length of a String
def string(name):
    return len(name)

name=input("Enter a string:")
print("Length of string:",string(name))
'''
Enter a string:hello
Length of string: 5
'''

# 9. Append to a List
def app(l1):
    l1.append(v)
    return l1
l1=list(map(int,input("Enter list Elements separated by space :").split()))
v=int(input("Enter element to append:"))
print("Updated list :",app(l1))
'''
Enter list Elements separated by space :1 2 3
Enter element to append:4
Updated list [1, 2, 3, 4]

'''
# 10. Double Each Element in a List
def list1(number):
     return [x * 2 for x in number]
    
number=list(map(int,input("Enter list elements :").split()))
print("Doubled list :",list1(number))
'''
Enter list elements :1 2 3
Doubled list : [2, 4, 6]
'''
# 11. Sort a List
def sort1(number):
    return sorted(number)

number=list(map(int,input("Enter list elements :").split()))
print("Sorted list :",sort1(number))
'''
Enter list elements :4 2 5 1
Sorted list : [1, 2, 4, 5]
'''
# 12. Clear a List Inside Function
def inside(number):
    number.clear()
    return number

number=list(map(int,input("Enter list Elements :").split()))
print("Cleared list:",inside(number))
'''
Enter list Elements :1 2 3
Cleared list: []

'''