#output Format

# Basic Examples of print()


# a) Printing Text
print("Hello World") #  Hello World

# b) Printing Multiple Items
name="manju"
age=22
branch='CSE'
print("name : ",name,"age : ",age,"branch : ",branch) # name :  manju age :  22 branch :  CSE

# c) Using sep to Change the Separator
print("10","7","2025", sep="-") # 10-7-2025

# print("Hello,", end=" ")
print("Hello.",end=" ") # Hello. 
print("World",end=" ") # World


# Printing Special Characters
# ● New Line (\n):
print("python \n program")
# python 
# program

# ● Tab (\t):  
print("Name : \t Manju") #  Name : 	 Manju


# Output Formatting
name="kowshik"   
age=22      
grade=9.5

# 1 Using Commas (Simple Print Method)

print("Name : ",name,"age :",age,"grade : ",grade) # Name :  kowshik age : 22 grade :  9.5

# 2 Using Commas (Simple Print Method)

name="abc"
score=89.66
age=34
print("Name: %s | Age: %d | Score: %.2f" %(name,age,score)) # Name: abc | Age: 34 | Score: 89.66

# 3 Using f-strings (Formatted String Literals) — Python 3.6+
print(f"Name: {name} | Age:{age} | Score: {score:.2f}") # Name: abc | Age:34 | Score: 89.66

# 4 Using str.format() Method
print("Name: {} | Age: {} | Score: {:.1f}".format(name,age,score)) # Name: abc | Age: 34 | Score: 89.7


a=10    
b=20    
c=30     
print("a:",a,"b:",b,"c",c) # a: 10 b: 20 c 30
print("a:%d | b: %d | c: %d"%(c,a,b)) # a:30 | b: 10 | c: 20

a,b,c=10,20,30  
print(a) # 10
print(b)# 20
print(c) # 30

