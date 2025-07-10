# List

# 2. Creating Lists

# 2.1 Empty List
li=[]
print(li) # []
my_list2=list()
print(my_list2) # []

# 2.2 List with Elements
n=[1,2,3,4,5]
print(n) # [1, 2, 3, 4, 5]
friuts=['apple','banana','cherry']
print(friuts) # ['apple', 'banana', 'cherry']

# 2.3 List with Nested Lists
nested_list=[[1,2,3],['a','b','c'],["A","B","C"]]
print(nested_list) # [[1, 2, 3], ['a', 'b', 'c'], ['A', 'B', 'C']]

# 2.4 List using list() Constructor
l3=(1,2,3,4,5)
print(l3) # (1, 2, 3, 4, 5)
print(type(l3)) # <class 'tuple'>

list(l3) # [1, 2, 3, 4, 5]
print(type([1, 2, 3, 4, 5])) # <class 'list'>

l4=list((1,2,3,4)) # Converting tuple to list
print(l4) # [1, 2, 3, 4]
print(type(l4)) # <class 'list'>

l5=list("java")
print(l5) # ['j', 'a', 'v', 'a']


# 3. Accessing Elements in a List

# 3.1 Using Indexing (Positive & Negative)
l6=["html","java","powerbi"]
print(l6) # ['html', 'java', 'powerbi']
print(type(l6)) # <class 'list'>

print(l6[0]) # html
print(l6[1]) # java
print(l6[2]) # powerbi
print(l6[-3]) # html
print(l6[-1]) # powerbi

# 3.2 Using Slicing
num=[60,70,80,90,100] 
print(num) # [60, 70, 80, 90, 100] 
print(type(num)) # <class 'list'>

print(num[1:5]) # [70, 80, 90, 100]
print(num[:5]) # [60, 70, 80, 90, 100]
print(num[4:]) # [100]
print(num[1:3]) # [70, 80]
print(num[-4:-1])# [70, 80, 90]
print(num[-1:]) # [100]
print(num[::-1]) # [100, 90, 80, 70, 60]

# 4. Modifying Lists

# 4.1 Changing Elements
num=[10,30,50,70]
print(num) # [10, 30, 50, 70]
print(type(num)) # <class 'list'>
num[2]=90
print(num) # [10, 30, 90, 70]
num[0]=100
print(num) # [100, 30, 90, 70]

# 4.2 Adding Elements
num=[10,11,12,13,14,15]
print(num) # [10, 11, 12, 13, 14, 15]
print(type(num)) # <class 'list'>

# Append (adds to the end)
num.append(17)
num.append(16)
print(num) # [10, 11, 12, 13, 14, 15, 17, 16]

# Insert (adds at a specific position)
num.insert(0,9)
num.insert(4,20)
print(num) # [9, 10, 11, 12, 20, 13, 14, 15, 17, 16]

# Extend (adds multiple elements)
num.extend([21,23,25])
num.extend([22,26])
print(num) # [9, 10, 11, 12, 20, 13, 14, 15, 17, 16, 21, 23, 25, 22, 26]

# 4.3 Removing Elements

 # Removes first occurrence.
num.remove(20)
num.remove(22)
print(num) # [9, 10, 11, 12, 13, 14, 15, 17, 16, 21, 23, 25, 26]

# Removes element at index 2
num.pop(2) # 11
print(num) # [9, 10, 12, 13, 14, 15, 17, 16, 21, 23, 25, 26]

# Removes last element
num.pop() # 26
print(num) # [9, 10, 12, 13, 14, 15, 17, 16, 21, 23, 25]

# Deletes element at index 
del num[2]
del num[5]
print(num) # [9, 10, 13, 14, 15, 16, 21, 23, 25]

# Clears the entire list
num.clear()
print(num) # []

# 5. List Methods

num=[3,5,7,4,9,8,6,2]
print(num) # [3, 5, 7, 4, 9, 8, 6, 2]
print(type(num)) # <class 'list'>

# count(x) 
print(num.count(1)) # 0
print(num.count(3)) # 1

# sort()
num.sort()
print(num) # [2, 3, 4, 5, 6, 7, 8, 9]

num.sort(reverse=True)# reverse
print(num) # [9, 8, 7, 6, 5, 4, 3, 2]

# index
print(num.index(3)) # 1

# reverse() 
num.reverse()
print(num) # [9, 8, 7, 6, 5, 4, 3, 2]

num1=[1,4,7,2,6,4]
print(num) # [9, 8, 7, 6, 5, 4, 3, 2]
sorted(num) # [2, 3, 4, 5, 6, 7, 8, 9]
max(num1) # 7
sorted(num1) # [1, 2, 4, 4, 6, 7]
min(num1) # 1
len(num1) # 6


