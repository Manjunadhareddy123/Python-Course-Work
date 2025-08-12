# 1. Print Numbers from 1 to N (Using for loop)
n=int(input("Enter the N value :"))
for i in range(1,n+1):
    print(i,end=" ")

# input :Enter the N value :10
# Output :0 1 2 3 4 5 6 7 8 9 10

# 2. Print Even Numbers from 1 to N (Using for loop)
n=int(input("Enter the N value :"))
for i in range(2,n+1):
    if i%2==0 :
        print(i,end=" ")
'''
Input :Enter the N value :20
Output :2 4 6 8 10 12 14 16 18 20 
'''
# 3. Sum of Numbers from 1 to N (Using for loop)
num=int(input("Enter the Number : "))
total=0
for i in range(1,num+1) :
    total+=i
print("Sum of numbers form 1 to",num,"is",total)
'''
Input :Enter the Number : 20
Output :Sum of numbers form 1 to 20 is 210
'''

# 4. Print Odd Numbers from 1 to N (Using for loop)
num=int(input("Enter the Number :"))
for i in range(1,num+1):
    if i%2==1 :
        print(i,end=" ")
'''
Input :Enter the Number :21
Output :1 3 5 7 9 11 13 15 17 19 21 
'''
n=int(input("Enter the number :"))

for j in range(2,n+1):
    c=0 
    for i in range(2,j//2+1):
        if j%i==0:
            c+=1
    if c==0 :
        print(f"{j}:prime number.")
'''
Input :Enter the number :9
Output
2:prime number.
3:prime number.
5:prime number.
7:prime number.
'''

# 5. Find Factorial of a Number (Using for loop)
num=int(input("Enter the Number :"))
if num>0:
    result=1
    for i in range(1,num+1):
        result *=i
    print(result)

'''
Input : Enter the Number :5
Output : 120
'''

# 6. Print Multiplication Table of N (Using for loop)
num=int(input("Enter the numbher :"))
table_number=int(input("Enter the number :"))
for i in range(1,num+1):
    print(table_number,"*",i,"=",table_number*i)

'''
Enter the numbher :10
Enter the number :12
12 * 1 = 12
12 * 2 = 24
12 * 3 = 36
12 * 4 = 48
12 * 5 = 60
12 * 6 = 72
12 * 7 = 84
12 * 8 = 96
12 * 9 = 108
12 * 10 = 120
'''

