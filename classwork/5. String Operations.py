 # 6. Introduction to Strings


str1="Hello World"
print("str1 :",str1) # str1 : Hello World
str2="Python programming language"
print("str2 : ",str2) # str2 :  Python programming language


# concatenation (+) -->  Joining two or more strings.
print(" Concatenation (+)",str1 + str2) #  Concatenation (+) Hello WorldPython programming language
str1='Manju'
str2='nadha'
str1+str2 # 'Manjunadha'
str3=str1+str2 
str3 # 'Manjunadha'
'python'+' programming' # 'python programming'

# Repetition (*) - Repeating a string multiple times.

print(str1) # Hello World
print("Repetition (*) : ",str1*4) # Repetition (*) :  Hello WorldHello WorldHello WorldHello World
p="python program language"
p #  'python program language'
p*3 # 'python program languagepython program languagepython program language'
"manju"*3 #  'manjumanjumanju'
"kowshik "*4 # 'kowshik kowshik kowshik kowshik '


# Indexing --> Accessing individual characters using indices.
str1="python programming"
print(str1) # python programming
str1[0] # 'p'
str1[-1] # 'g'
str1[5] # 'n'
str1[8] # 'r'
str1[7] # 'p'
str1[-3] # 'i'

#Slicing --> Extracting a part (substring) of the string.

print(str2) # Python programming language
print(str2[0:5]) # Pytho
print(str2[ :5]) # Pytho
print(str2[0:6]) # Python
print(str2[-1:]) # e
print(str2[ :-1]) # Python programming languag
print(str2[ : ]) # Python programming language
print(str2[5: ]) # n programming language
 
# Membership --> (in, not in) - Checking if a substring exists within a string.
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
names="Python programming language"
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

# sorted() 
a="manjunadha"
print(type(a)) # <class 'str'>
print(sorted(a)) # ['a', 'a', 'a', 'd', 'h', 'j', 'm', 'n', 'n', 'u']

# str1="Hello World")
# ord --> chr() / ord() - Converts between characters and their ASCII codes.
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

# Upper() --> Converts all characters to uppercase.
names.upper() # 'PYTHON PROGRAMMING LANGUAGE'
d.upper() # 'PYTHONPROGRAMMINGLANGUAGE'
'python'.upper() # 'PYTHON'

# lower() --> Converts all characters tolowercase.

names.lower() # 'python programming language'
d.lower() # 'pythonprogramminglanguage'
"PYTHON".lower() # 'python'

# Capitalize() --> Capitalizes the first character.  
f='welcome to python classes'
print(f) # welcome to python classes
f.capitalize() # 'Welcome to python classes'
"manju nadha".capitalize() # 'Manju nadha'

# Title() --> Capitalizes the first letter of each word.
print(f) # welcome to python classes
f.title() # 'Welcome To Python Classes'
"manju nadha".capitalize() # 'Manju nadha'
"manju nadha".title() # 'Manju Nadha'

# swapcase() --> Swaps case: upper → lower, lower → upper
print(f) # welcome to python classes
f.swapcase() # 'WELCOME TO PYTHON CLASSES'
g="Welcome To Python Class"
print(g) # Welcome To Python Class
g.swapcase() # 'wELCOME tO pYTHON cLASS'
h="Python Programming Language"
"Python Programming Language".swapcase() # 'pYTHON pROGRAMMING lANGUAGE'
"manju".swapcase() # 'MANJU'
"MANJUNADHA".swapcase() # 'manjunadha'

# casefold() --> Converts to lowercase (more aggressive than lower()).
"ß".casefold() # 'ss'
"MANJU".casefold() # 'manju'


# 2. Alignment & Formatting Methods

str1="python programming"
str1 # 'python programming'

# center(width,fillchar) --> Centers the string within width.

str1.center(20,"*") # '*python programming*'
len(str1) # 18
str1.center(50,"*") # '****************python programming****************'
str1.center(40,"-") # '-----------python programming-----------'
"manju".center(30,"#") # '############manju#############'
"nadha".center(30,"2") # '222222222222nadha2222222222222'

# ljust(width,fillchar) --> Left-aligns the string within width.

str1.ljust(30,"&") # 'python programming&&&&&&&&&&&&'
"manju".ljust(30,"^") # 'manju^^^^^^^^^^^^^^^^^^^^^^^^^'

# rjust(width,fillchar) -->Right-aligns thestring within width.
str1.rjust(30,'&') # '&&&&&&&&&&&&python programming'
"python".rjust(30,"%") # '%%%%%%%%%%%%%%%%%%%%%%%%python'

# zfill(width) --> Pads the string withzeros on the left.

"42".zfill(5) # '00042'
"568".zfill(7) # '0000568'
d='python'
d.zfill(10) # 0000python'


# 3. Search & Find Methods

# find(sub) --> Returns the index of first occurrence, -1 if not found.

str1="ManjuKowshikKiran"
str1 # 'ManjuKowshikKiran'
str1.find("Manju") # 0
str1.find("Kowshik") # 5
str1.find("Kiran") # 12
str1.find('K') # 5
"python".find('h') # 3
str1.find('m') # -1

# rfind(sub) --> Returns the last occurrence of the substring. 
str1.rfind('K') # 12
str1.rfind("M") # 0
"programming".rfind('m') # 7

# index(sub) --> Like find(), but raises an error if not found.
str1 # 'ManjuKowshikKiran'
str1.index("K") # 5
str1.index('w') # 7
"python".index('h') # 3
"pyhon".index('ho') # 2

# rindex(sub) --> Like rfind(), but raises an error if not found.

str1.rfind('iran') # 13
str1.rindex('ira') # 13
"programming".rindex("m") # 7

# count(sub) --> Counts how many times sub appears. 
str2='pythonprogramming'
str2 # 'pythonprogramming'
str2.count('p') # 2

str2.count('K') # 0
sorted(str2) # ['a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']


#  4. String Testing Methods (Boolean Results)

# startswith(sub)  --> Checks if the string starts with sub.

str1='DS-15','DS-14','DA-15','DA-14','PFS-16','PFS-15'
str1 # ('DS-15', 'DS-14', 'DA-15', 'DA-14', 'PFS-16', 'PFS-15')

for i in str1 :
    if i.startswith('DS'):
        print(i)     
# DS-15
# DS-14

for i in str1 :
    if i.startswith('DA'):
        print(i)      
 # DA-15
# DA-14

for i in str1 :
    if i.startswith('PFS'):
        print(i)      
# PFS-16
# PFS-15
"python".startswith("Py") # False
"python".startswith("py") # True

# endswith(sub) --> Checks if the string ends with sub.

strt1="python.py","str11.py","first.html","second.java"
strt1 # ('python.py', 'str11.py', 'first.html', 'second.java')

for i in strt1 :
    if i.endswith('.py'):
        print(i)     
# python.py
# str11.py

for i in strt1 :
    if i.endswith('.html'):
        print(i)       
# first.html

"demo.java".endswith(".java") # True

# isalpha()  --> Returns True if all characters are alphabets.
"manju".isalpha() # True
"KOWSHIK".isalpha() # True
"nadha123".isalpha() #  False

# isalnum() --> Returns True if all characters are alphanumeric.

"manju123".isalnum() # True
"1234".isalnum() # True
"manju".isalnum() # True
"manju@123".isalnum() # False

# islower() --> Returns True if all characters are lowercase.
"Python".islower() # False
"python".islower() # True
"py123".islower() # True

# isupper() --> Returns True if all characters are uppercase
"MANJU".isupper()# True
"mANJU".isupper() # False
"MANJU123".isupper() # True

# isspace() --> Returns True if all characters are whitespace.
"python programming".isspace() # False
"manju  nadha".isspace() #  False
"manju".isspace() # False
"manju nadha".isspace() # False
" manju".isspace() # False
"nadha ".isspace()# False

# istitle() --> Returns True if the string is in the title case.

"Python programming".istitle()# False
"Python Programming".istitle() # True

# isidentifier() --> Checks if the string is a valid Python identifier
"manju@123".isidentifier() # False
"variable1".isidentifier() # True
"manju123".isidentifier() # True

# 5. Replace & Modify Methods
m="manju"
m # 'manju'
# replace(old,new)--> Replaces occurrences ofold with new.

m.replace('u','unadha') # 'manjunadha'
"pythont".replace('t',' program') # 'py programhon program'
"pyhon".replace('y','yt') # 'python'

#translate(table)--> Replaces characters using a translation table.

pass1='manju@123'
print(pass1)  #'manju@123'
pass1.translate(str.maketrans("@123","#234")) # 'manju#234'
pass1.translate(str.maketrans("manju","nadha")) # 'nadha@123'
"pythonpp".translate(str.maketrans('pp','.p')) # 'pythonpp'
"pythonpp".translate(str.maketrans('pp','bb')) # 'bythonbb'

# maketrans() --> Creates a translation tablenfor translate().

"manju@123".maketrans('@123','#123')
{64: 35, 49: 49, 50: 50, 51: 51}


# 6. Splitting & Joining Methods
# split(sep) --> Splits the string into a list by sep.

s=" my name is kotikrian"
s.split() # ['my', 'name', 'is', 'kotikrian']
s.split('@') # [' my name is kotikrian']
s.split('a') # [' my n', 'me is kotikri', 'n']
"manjunadha".split('a') # ['m', 'njun', 'dh', '']
i='manju,nadha,reddy'
print(i) # 'manju,nadha,reddy'
i.split(',') # ['manju', 'nadha', 'reddy']

# rsplit(sep)--> Splits from the right side.

s.rsplit('a',2) # [' my n', 'me is kotikri', 'n']
"manjunadha".rsplit('a',2) # ['manjun', 'dh', '']
"manjunadha".split('a',2) # ['m', 'njun', 'dha']

# splitlines() --> Splits at line breaks (\n).

file='''Hello
world
Python
programming'''
file # 'Hello\nworld\nPython\nprogramming'
file.splitlines() # ['Hello', 'world', 'Python', 'programming']
'Hello\nworld\nPython\nprogramming'.split('\n') # ['Hello', 'world', 'Python', 'programming']

# join(iterable) --> Joins elements with a separator.

"['Hello', 'world', 'Python', 'programming']".join(',') #','
",".join(['Hello', 'world', 'Python', 'programming'])# 'Hello,world,Python,programming'
"#".join(['Hello', 'world', 'Python', 'programming']) # 'Hello#world#Python#programming'
" @ ".join(['Hello', 'world', 'Python', 'programming']) # 'Hello @ world @ Python @ programming'

# partition(sep) --> Splits into a 3-part tuple at first sep.

"python.py".partition('.') # ('python', '.', 'py')
"python.program.py".partition('.') # ('python', '.', 'program.py')

# rpartition(sep) --> Splits into a 3-part tuple at last sep.

"python.program.py".rpartition('.') # ('python.program', '.', 'py')
"world.python.program.hello".rpartition('.') # ('world.python.program', '.', 'hello')

 
#  7. Whitespace & Trimming Methods
# strip(chars) --> Removes leading and trailing characters (default: spaces).

"     manju     ".strip() # 'manju'
"  Hello world     ".strip() # 'Hello world'
m="   python    "
print(m) # '   python    '
m.strip() # 'python'
"------manju-----".strip('-') # 'manju'

# lstrip(chars) --> Removes leading characters. 
m.lstrip() # 'python    '
"       manju        ".lstrip() # 'manju        '

# rstrip(chars) --> Removes trailing characters. 
m.rstrip() # '   python'
"       manju        ".rstrip() # '       manju'


# 8. Encoding & Decoding Methods

# encode(encoding) --> Converts the string tobytes.

text="manjunadha"
print(text) # 'manjunadha'
text.encode() # b'manjunadha'
text = "Hello नमते你好 café 🙂"

print(text) #'Hello नमते你好 café 🙂'
text.encode() # b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'

# decode(encoding) -->  Converts bytes back tostring.

b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'.decode() # 'Hello नमते你好 café 🙂'
