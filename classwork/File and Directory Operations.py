# File and Directory Operations
# 1. File Operations
# 1.1 Opening a File
# read file
try:
    file=open("demo.txt","r")
except FileNotFoundError :
    print("File is not present")
else :
    read=file.read()  # read total content
    file.seek(0) # return to first line.

    readlines=file.readlines() # read the content \n lines all
    file.seek(0)

    readline=file.readline() # read only first line
    print(f"\nFile Content using read():\n{read}")
    print(f"\nFile Content using readlines():\n{readlines}")
    print(f"\nFile Content using readline():\n{readline}")
    file.close()
finally :
    print("Rest of the code")

'''
Output :
-----------------------------------------------

File Content using read():
manju
laddu
kiran
teja

File Content using readlines():
['manju\n', 'laddu\n', 'kiran\n', 'teja']

File Content using readline():
manju

Rest of the code
'''

# Writing to a File
# if file is not having , it will create the file. it will write content.

try:
    file=open("dsda.txt","w")
except FileNotFoundError :
    print("File is not present")
else :
    file.write('Monday we have Exam.')
    file.close()

finally :
    print("Rest of the code")



try:
    file=open("dsda.txt","w+")
except FileNotFoundError :
    print("File is not present")
else :
    file.write('Monday we have Exam.')
    file.seek(0)
    print(file.read())
    file.close()

finally :
    print("Rest of the code")

# pending a,r+,a+

'''
r -read
w-write
a-append
r+ -read + write
w+ -write + read
+ -append + read

'''
# rewrite the content
# already having content can remove and new content will be added.

with open('dsda.txt','r+')as file:
    file.write('\n File operations.')
    file.seek(0)
    print(file.read())

'''
 File operations..
'''

# Create a directay/folder
import os
print(os.getcwd()) # getcwd --> get current working directory.
if not os.path.exists('DSDA'):
    os.mkdir('DSDA')
'''
'''
# used to remove empty directories
import os
if  os.path.exists('DSDA'):
    os.rmdir('DSDA')

import os
if not os.path.exists('DSDA'):
    os.mkdir('DSDA')
os.makedirs('DSDA/1415')


# remove the floder in folder in data ,remove the total outer folder
# there is no content
import os
import shutil

if not os.path.exists('DSDA'):
    os.mkdir('DSDA')
    os.makedirs('DSDA/1415')

shutil.rmtree('DSDA')

