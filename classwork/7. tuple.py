# Tuples


# 1. Introduction to Tuples

# Tuple Creation Syntax:
# Empty Tuple
t1=()
print("t1",t1) # t1 ()
print(type(t1)) # <class 'tuple'>
t2=tuple() 
print("t2",t2) # t2 ()
print(type(t2)) # <class 'tuple'>

# Single-element Tuple (note the trailing comma)
t3=(5,)
print('t3',t3) # t3 (5,)

# Multi-element Tuple
t4=(1,2.3,3+4j,True,"manju",(1,2,3))
print("t4 :",t4) # t4 : (1, 2.3, (3+4j), True, 'manju', (1, 2, 3))

# Without parentheses (implicit tuple creation)
t5=1,2,3,4,5
print('t5 :',t5) # t5 : (1, 2, 3, 4, 5)
print(type(t5)) # <class 'tuple'>


# 2. Accessing Tuple Elements
# a. Indexing
t11=(10,15,20,25,30)
print("t11",t11) # t11 (10, 15, 20, 25, 30)
print(t11[3]) # 25
print(t11[2]) # 20

# b. Negative Indexing
print(t11[-3]) # 20
print(t11[-1]) # 30

# c. Slicing
print(t11[2::2]) # (20, 30)
print(t11[2:]) # (20, 25, 30)
print(t11[:-3]) # (10, 15)


# 3. Operations on Tuples
# a. Concatenation
t12=(1,2,3)
print('t12 :',t12) # t12 : (1, 2, 3)
t13=(4,5,6) #
print('t13 :',t13) # t13 : (4, 5, 6)
t14=t12+t13
print('t14 :',t14) # t14 : (1, 2, 3, 4, 5, 6)

# b. Repetition
print(t12*3) # (1, 2, 3, 1, 2, 3, 1, 2, 3)
print('t13 :',t13*3) # t13 : (4, 5, 6, 4, 5, 6, 4, 5, 6)

# c. Membership Testing
t15=(1,5,10,15,20,25,30)
print('t15',t15) # t15 (1, 5, 10, 15, 20, 25, 30)

# in
print("5 in t15",5 in t15) # 5 in t15 True
print("6 in t15 : ",6 in t15) # 6 in t15 :  False
print("20 in t15 : ",20 in t15) # 20 in t15 :  True

# not in
print("6 not in t15 : ",6 not in t15)# 6 not in t15 :  True
print("20 not in t15 : ",20 not in t15) # 20 not in t15 :  False

# d. Tuple Unpacking
t16=(1,2,3,4)
print('t16',t16) # t16 (1, 2, 3, 4)
a,b,c,d=t16
print('a,b,c,d',a,b,c,d) # a,b,c,d 1 2 3 4
print('a',a) # 1
print('b',b) # 2

# 4. Tuple Methods
t16.count(4) # 1 count
print("t16.count(3)",t16.count(3)) # 1 count
print("t16.index(2)",t16.index(2)) # 1 index
print("t16.index(3)",t16.index(3)) # 2 index

# 5. Built-in Functions for Tuples
print("len of t16 ",len(t16)) # len of t16  4
print("max of t16 :",max(t16)) # max of t16 : 4
print("min of t16 :",min(t16)) # min of t16 : 1
print("sum of t16 :",sum(t16)) # sum of t16 : 10

print("string to tuple :",tuple([1,2,3,4])) #  string to tuple : (1, 2, 3, 4)

# 6. Immutability and Tuple Behavior
t21=(2,3,[4,5,6])
print('t21 :',t21) # t21 : (2, 3, [4, 5, 6]) 
t21[2][1]=100
print("t21 :",t21) # t21 : (2, 3, [4, 100, 6])
