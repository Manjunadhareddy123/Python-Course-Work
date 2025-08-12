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
# functions

# 13. Update Dictionary Value
def update_dict_value(d, key, new_value):
    d[key] = new_value
    return d
dict_input = input("Enter dictionary: ")
key = input("Enter key to update: ")  
value = input("Enter new value: ") 

d = eval(dict_input)

if value.isdigit():
    value = int(value)

updated_dict = update_dict_value(d, key, value)

print("Updated dictionary:", updated_dict)
'''
Input :
Enter dictionary: {'a':1}
Enter key to update: a
Enter new value: 2

Output :
Updated dictionary: {'a': 2}
'''


# 14. Remove Element from List by Value
def remove_element(lst, value):
    if value in lst:
        lst.remove(value)
    return lst
input_list = input("Enter list elements: ")   
element_to_remove = input("Enter element to remove: ") 

lst = list(map(int, input_list.split()))
value = int(element_to_remove)

updated_list = remove_element(lst, value)
print("Updated list:", updated_list)

'''
Input :
Enter list elements: 1 2 3 4
Enter element to remove: 3

Output :
Updated list: [1, 2, 4]
'''

# 15. Add Key to Dictionary
def add_key(d,key,value):
    d[key]=value
    return d

dict_input=input("Enter the dict :")
new_key=input("Enter the new key :")
new_value=input("Enter the new value :")

d=eval(dict_input)

if new_value.isdigit():
    new_value=int(new_value)
update=add_key(d,new_key,new_value)

print("Updated dicionary :",update)
'''
Input :
Enter the dict :{'x':10}
Enter the new key :y
Enter the new value :20

Output :
Updated dicionary : {'x': 10, 'y': 20}

'''

# 16. Increment All Values in Dictionary
def increment_values(d):
    for key in d:
        d[key]+=1
    return d
dict_input=input("Enter Dicionary :")
d=eval(dict_input)
update1=increment_values(d)
print("Updated dictionary :",update1)
'''
Input : Enter Dicionary :{'a':1,'b':2}
Output : Updated dictionary : {'a': 2, 'b': 3}
'''

# 17. Factorial of a Number
def fact(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
num=int(input("Enter the number :"))
a=fact(num)
print(a)
'''
Input : Enter the number :5
Output :120
'''

# 18. Fibonacci Number (Nth Term)
def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

term=int(input("Enter the Fibonacci number :"))
fib_number=fibonacci(term)

print("Fibonacci numberis :",fib_number)
'''
Input : Enter the Fibonacci number :6
Output : Fibonacci numberis : 8
'''
# 19. Sum of First N Natural Numbers
def sum_natural(n):
    return n*(n+1)//2
num=int(input("Enter a number :"))
total=sum_natural(num)
print("Sum of natural numbers :",total)
'''
Input : Enter a number :10
Output : Sum of natural numbers : 55
'''
#20. Reverse a String Using Recursion

def reverse_string(s):
    if len(s)==0:
        return s
    return reverse_string(s[1:])+s[0]
text=input("Enter the string :")
reverse_text=reverse_string(text)

print("Reversed string is :",reverse_text)
'''
Input : Enter the string :hello
Output : Reversed string is : olleh
'''
