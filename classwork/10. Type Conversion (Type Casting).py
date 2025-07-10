# Type Conversion (Type Casting)

# 1 Converting from int

a=10 
print(a) # 10
print(type(a)) # <class 'int'>
float(a) # 10.0
str(a) # '10'
bool(a) # True
# list(a) --> type error
# tuple(a)--> type error
# set(a) --> type error
# dict(a)-->type error

# 2. Converting from float

b=20.3
print(b) #  20.3
print(type(b)) # <class 'float'>

int(b) #20
print(type(20)) # <class 'int'>
str(b) # '20.3'
print(type('20.3')) # <class 'str'>
complex(b) # (20.3+0j)
print(type((20.3+0j))) # <class 'complex'>
bool(b) # True
print(type(True)) # <class 'bool'>
# tuple(b) --> Type error
# set(b) --> Type error
# list(b) --> Type error
# dict(b) --> Type error

# 3. Converting from str

str='10'
print(str) #  10
print(type(str)) # <class 'str'>
int(str) # 10
print(type(10)) # <class 'int'>

float(str) # 10.0
print(type(10.0))# <class 'float'>

str1="python" 
str1 # 'python'
list(str1) # ['p', 'y', 't', 'h', 'o', 'n']
bool(str) # True
print(type(True))# <class 'bool'>
list(str) # ['1', '0']


str.split() # ['10']
str1="manju"
print(str1) # manju
print(type(str1)) # <class 'str'>
list(str1) # ['m', 'a', 'n', 'j', 'u']
tuple(str1) # ('m', 'a', 'n', 'j', 'u')
set(str1) #{'u', 'j', 'a', 'm', 'n'}
# dict(str1) --> value erroe

# 4. Converting from list

l=[1,2,3,4,5,6,7]
print(l) # [1, 2, 3, 4, 5, 6, 7]
print(type(l)) # <class 'list'>
# int(l)--> TypeError:
# float(l) --> TypeError:
#complex(l) --> TypeError:
bool(l) # True

b2=["java","python","html"]
print(b2) # ['java', 'python', 'html']
print(type(b2)) #  <class 'list'>
 # str(l) # '[1, 2, 3, 4, 5, 6, 7]'
# str(b2) #"['java', 'python', 'html']"
''.join(b2) # 'javapythonhtml'
# str(b2)  "['java', 'python', 'html']"
tuple(b2) # ('java', 'python', 'html')
set(b2) # {'html', 'java', 'python'}
b3=[(1,2),(3,4),(5,6)]
print(b3) # [(1, 2), (3, 4), (5, 6)]
print(type(b3)) # <class 'list'>
dict(b3) # {1: 2, 3: 4, 5: 6}
print(type(b3)) # <class 'list'> '''

# 5. Converting from tuple
t1=(1,2,3,4,5)
print(t1) # (1, 2, 3, 4, 5)
print(type(t1)) # <class 'tuple'>
# int(t1)--> TypeError: 
# float(t1) --> TypeError: 
# complex(t1) --> TypeError: 
bool(t1) # True
str(t1)#'(1, 2, 3, 4, 5)'
list(t1) # [1, 2, 3, 4, 5]
type(t1) # <class 'tuple'>

set(t1) # {1, 2, 3, 4, 5}

t2=[(1,2),(3,4),(5,6)]
print(t2) # [(1, 2), (3, 4), (5, 6)]
print(type(t2)) # <class 'list'>
dict(t2) #{1: 2, 3: 4, 5: 6}
t3=(1,2,3,4)

# 6. Converting from set

s1={1,2,3,4,5}
print(s1) # {1, 2, 3, 4, 5}
print(type(s1)) # <class 'set'>
# int(s1) --> TypeError:
# float(s1) --> TypeError:
# complex(s1) --> TypeError:
bool(s1) # True

str(s1) # '{1, 2, 3, 4, 5}'
list(s1)# [1, 2, 3, 4, 5]
tuple(s1) # (1, 2, 3, 4, 5)
# dict(s1)--> TypeError:

# 7. Converting from dict

d1={1:2,3:4,5:6}
print(d1) # {1: 2, 3: 4, 5: 6}
print(type(d1)) # <class 'dict'>
# int(d1) --> TypeError:
# float(d1) --> TypeError:
# complex(d1) --> TypeError:
bool(d1) # True
# str(d1) # '{1: 2, 3: 4, 5: 6}'
list(d1)

tuple(d1) # (1, 3, 5)
set(d1) # {1, 3, 5}'''
