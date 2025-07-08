# 4.pYTHON operators.py
# 4. Python Operators.py

# 1. Arithmetic Operators
a=20
b=10
print("Addition(+) :",a+b) # Addition(+) : 30
print("Subtraction(-) :",a-b) # Subtraction(-) : 10
print("Multiplication(*) :",a*b) # Multiplication(*) : 200
print("division(/) :",a/b) # division(/) : 2.0
print("Floor Division(//) :",a//b) # Floor Division(//) : 2
print("Modulus(%) :",a%b) # Modulus(%) : 0
print("Exponentiation(**) :",a**b) # Exponentiation(**) : 10240000000000

# 2 Comparison Operator

print("Equal to (==) :",a==b) # Equal to (==) : False
print("Not Equal to(!=) :",a!=b) # Not Equal to(!=) : True
print("Greater than (>) :",a>b) # Greater than (>) : True
print("Less than (<) :",a<b) # Less than (<) : False
print("Greater than or Equalto(>=) :",a>=b) # Greater than or Equalto(>=) : True
print("Less than or Equal to (<=) :",a<=b) # Less than or Equal to (<=) : False

# 3 Assignment Operators.

# Assign 
a=20 # a  20

# Add & Assign 
a=20 # a  20
a+=10 # a 30
a=a+40 # a 70

# Subtract & Assign
b=50 # b 50
b-=10 # b 40
b=b-20 # b 20
b=10-b # b -10

# Multiply & Assign
c=20 # c 20
c*=10 # c 200
c=c*20 # c 4000
c=5*c # c 20000

# Divide & Assign
d=60 # d 60
d/=6 # d 10.0
d=d/5 # d 2.0

# Floor Divide & Assign 
e=400 # e 400
e//=5 # e 80
e=e//5 # e 16

# Modulus & Assign 
f=500 # f 500
f%=6 # f 2

# Exponentiate & Assign
g=40 # g 40
g=g**2 # g 1600
g**=3 # g 4096000000


# 4 Logical Operators (Using Logic Gates)


# And
x=20
y=40
print(x<y and x<y) # True
print(x>y and x<y) # False
print(x>10 and y>x) # True
print(x<40 and 100>y) # True

# Or
x=10
y=20
print(x<y or y>x) #True
print(x<y or x>y) #True
print(x>y or x<y) # True
print(x>y and y<x)# False

# Not
a=20
print(not(x>5)) # False
print(not(x)) # False
print(not(x<5)) #True


# 5. Membership Operators


# In
names=['manju','kowshik','Laddu','Gopal'] 
names # ['manju', 'kowshik', 'Laddu', 'Gopal']
print("manju" in names) #True
print("Gopal" in names) # True
print("Manju" in names) # False
print("siva" in names) # False
print("kowshik" in names) # True

# Not in
names # ['manju', 'kowshik', 'Laddu', 'Gopal']
print("Manju" not in names) # True
print("manju" not in names) # False
print("kowshik" not in names) # False
print("Ravindra" not in names) # True


# 6. Identity Operators


# Is
a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=[6,7,8,9,10]
d=[3,4,5,6,7]
e=a
print(a,b,c,d,e) #[1, 2, 3, 4, 5] [1, 2, 3, 4, 5] [6, 7, 8, 9, 10] [3, 4, 5, 6, 7] [1, 2, 3, 4, 5]
print(id(a)) # 1747069067456
print(id(b)) # 1747069024128
print(id(c)) # 1747113561792
print(id(d)) # 1747113258304
print(id(e)) # 1747069067456
print(a is b) # False
print(a is e) #True
print(a is c) # False
print( c is d) # False

# is not
print(a,b,c,d,e) #[1, 2, 3, 4, 5] [1, 2, 3, 4, 5] [6, 7, 8, 9, 10] [3, 4, 5, 6, 7] [1, 2, 3, 4, 5]
print(a is not b) # True
print(a is not e) # False
print("7" is not a) # True
print("3" is not b) # True
print(3 is not a) # True
print("5" is not a) # True
print(c is not a) # True

# 7. Bitwise Operators (With Binary Representation

a=10
b=15
print(a,b) # 10 15
print(a & b) # 10
print("or",a|b) # or 15
print("xor : ",a^b)# xor :  5

#left Shift(>>)
32>>1 # 16
16>>2 # 4
16>>1 # 8
8>>1 # 4
4>>1 # 2
2>>1 # 1
32>>2 # 8
16>>2 # 4
4>>2 # 1
32>>3 # 4

# Right Shift
2<<1 # 4
4<<1 # 8
8<<1 # 16
16<<1 # 32
4<<3 # 32
