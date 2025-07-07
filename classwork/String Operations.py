# 6. Introduction to Strings


str1=("Hello World")
print("str1 :",str1) # str1 : Hello World
str2=("Python programming language")
print("str2 : ",str2) # str2 :  Python programming language
print(" Concatenation (+)",str1 + str2) #  Concatenation (+) Hello WorldPython programming language
print(str1) # Hello World
print("Repetition (*) : ",str1*4) # Repetition (*) :  Hello WorldHello WorldHello WorldHello World

# Indexing
print(str1[0]) # H
print(str1[-2]) # l
print(str1[8]) # r
print(str1[6]) # W

#Slicing  
print(str2) # Python programming language
print(str2[0:5]) # Pytho
print(str2[ :5]) # Pytho
print(str2[0:6]) # Python
print(str2[-1:]) # e
print(str2[ :-1]) # Python programming languag
print(str2[ : ]) # Python programming language
print(str2[5: ]) # n programming language
 
# Membership
#In
print(str1) # Hello World
print('Hello' in str1) # True
print('hello' in str1) # False
print('e' in str1) # True
print('z' in str1) # False

#Not in
print('Hello' not in str1)# False
print('c' not in str1) # True
print('java' not in str1) # True


#  Built-in String Functions


print(names) # Python programming language
d='PythonProgrammingLanguage'
print(d) # PythonProgrammingLanguage

#len()
len(names) # 27
len("python") # 6
len('python python') # 13

#max()
max(names) # 'y'
max("manju") # 'u'
min(names) # ' '

#min()
min(d) # 'L'
min('manju') # 'a'

# str1="Hello World")
# ord
ord('a') # 97
ord('A') # 65
ord('*') # 42
ord('L') # 76

#chr()
chr(65) # 'A'
chr(98) # 'b'
chr(43) # '+'

#  Complete List of Python String Methods with Examples
# 1. Case Conversion Methods
d='PythonProgrammingLanguage'
print(d) # PythonProgrammingLanguage
names='Python Programming language'
print(names) # Python Programming language

# Upper()
names.upper() # 'PYTHON PROGRAMMING LANGUAGE'
d.upper() # 'PYTHONPROGRAMMINGLANGUAGE'
'python'.upper() # 'PYTHON'

# lower()
names.lower() # 'python programming language'
d.lower() # 'pythonprogramminglanguage'
"PYTHON".lower() # 'python'
f='welcome to python classes'
print(f)
f.capitalize()

