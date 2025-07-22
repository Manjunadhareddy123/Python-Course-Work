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
