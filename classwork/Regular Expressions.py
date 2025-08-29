# Regular Expressions (RegEx)

# re.match() --> Checks if the pattern matches only at the start of the string.

import re
res=re.match(r'[a-z]','helloworld')  # only first letter can be given.
print(res.group() if res else "No pattern")
'''
h
'''

import re
res=re.match(r'[a-z]+','helloworld') # given the first word only.
print(res.group() if res else "No pattern")
'''
helloworld
'''
import re
res=re.match(r'[\d]','helloworld') # start with only digit. other wise given the No pattern else statement.
print(res.group() if res else "No pattern")
'''
No pattern
'''

import re
res=re.match(r'[\d]','2343helloworld')
print(res.group() if res else "No pattern")
'''
2
'''


#  re.search() --> Searches for the first occurrence of the pattern anywhere inthe string.

import re
res=re.search(r'[0-9]{2}','ds-da-15-14') # search in string.
# [] --> at least one letter.
# {}--> given the no of letters occuer.
print(res.group() if res else "No pattern")
'''
15
'''

import re
res=re.search(r'[a-z]{2}','ds-da-15-14')
print(res.group() if res else "No pattern")
'''
ds
'''

import re
res=re.search(r'[a-z]{2}','HELLO WORLD')
print(res.group() if res else "No pattern")
'''
No pattern
'''

import re
res=re.search(r'[a-z]{2}','HELLO world')
print(res.group() if res else "No pattern")
'''
wo
'''

import re
res=re.search(r'[A-Z]{2}','HELLO world')
print(res.group() if res else "No pattern")
'''
HE
'''

import re
res=re.search(r'[A-Z]+','HELLO world')
print(res.group() if res else "No pattern")
'''
HELLO
'''

# re.findall() -->  Returns all matches in a list.
import re
res=re.findall(r'[0-9]{2}','PFS-30 & PFS-31 & DS-DA-15-14')
print(res)
'''
['30', '31', '15', '14']
'''

import re
res=re.findall(r'[A-Z]{2}','PFS-30 & PFS-31 & DS-DA-15-14')
print(res)
'''
['PF', 'PF', 'DS', 'DA']
'''

# . --> given the any letter,digit,symbol
import re
res=re.findall(r'p..h.n','python pythox psthon psxhin')
print(res)
'''
['python', 'psthon', 'psxhin']
'''

import re
res=re.findall(r'h..','hii hot hop hipp hatt')
print(res)
'''
['hii', 'hot', 'hop', 'hip', 'hat']
'''

# re.finditer() --> Returns an iterator of match objects.
import re
res = re.finditer(r'[A-Z]{2}', 'PFS-30 & PFS-31 & DS-DA-15-14')  
# Based on the position a index of string.
for i in res:
    print(i.group(), i.start())

'''
PF 0
PF 9
DS 18
DA 21
'''

import re
res = re.finditer(r'[A-Z]{2}', 'PFS-30 & PFS-31 & DS-DA-15-14')
for i in res:
    print(i.group(), i.end())

'''
PF 2
PF 11
DS 20
DA 23
'''

# re.fullmatch()  -->  Checks if the entire string matches the pattern.

# Enter string can be match with given expression  "same as same " same position also
# + --> atleast one item or more items
# * --> option
# . --> any random number special charters

import re
res=re.fullmatch(r'(aeiou)','aeiou')
print(res.group() if res else "No  pattern")
'''
aeiou
'''

import re
res=re.fullmatch(r'(aeiou)','aeiouaeiou')
print(res.group() if res else "No  pattern")
'''
No  pattern
'''

import re
res=re.fullmatch(r'(aeiou)+','aeiouaeiou')
print(res.group() if res else "No  pattern")
'''
aeiouaeiou
'''

import re
res=re.fullmatch(r'(aeiou)*','aeiouaeiou')
print(res.group() if res else "No  pattern")
'''
aeiouaeiou
'''

import re
res=re.fullmatch(r'(aeiou)*','')
print(res.group() if res else "No  pattern")

'''

'''

import re
res=re.fullmatch(r'\d{10}','9876543210')
print(res.group() if res else "No  pattern")
'''
9876543210
'''

import re
res=re.fullmatch(r'\d{10}','98765432')
print(res.group() if res else "No  pattern")
'''
No  pattern
'''

import re
res=re.fullmatch(r'[6-9]\d{10}','0987654321')
print(res.group() if res else "No  pattern")
'''
No  pattern
'''

import re
res=re.fullmatch(r'[6-9]\d{9}','9876543210')
print(res.group() if res else "No  pattern")
'''
9876543210
'''

# re.split() --> Splits a string at each match.

import re
res=re.split(r'[; - _ ,]','python;pythox-python0"python1-')
print(res)
'''
['python', 'pythox-python0"python1-']
'''

# re.sub() --> Replaces matches with another string.

import re
res=re.sub(r'[aeiouAEIOU]','*','python programming Language')
print(res)
'''
pyth*n pr*gr*mm*ng L*ng**g*
'''

import re
res=re.sub(r'[aeiouAEIOU23]','*','python programming Language 123adhghj111')
print(res)
'''
pyth*n pr*gr*mm*ng L*ng**g* 1***dhghj111
'''

import re
res=re.findall(r'\b\d{2}\b','34 56 78 90 100 120 145 123 22 21 33')
print(res)
'''
['34', '56', '78', '90', '22', '21', '33']
'''