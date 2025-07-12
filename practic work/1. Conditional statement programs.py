# 1. Conditional statement programs



# 1. Positive or Negative
num=int(input("Enter the NUmber :"))
if num>0 :
    print("Positive Number")
elif num< 0:
    print("Negative number")
else :
    print("Zero")
    

# 2. Even or odd
while True :
    num=int(input("Enter the number :"))
    if num%2==0 :
        print("Even number :",num)
    elif num%2==1 :
        print("Odd number :",num)
    else :
        print("Zero")

# 3 Divisile by 5
while True :
    num= int(input("Enter the number :"))
    if num%5==0 :
        print(num,"is divisible by 5")
    else :
        print(num,"is not divisible by5")

# 4. Divisible by 3 and 7
num=int(input("Enter the Number :"))
if num % 3==0 and num % 7 ==0:
    print(num,"is divisible by both 3 and 7")
else :
    print(num,"is nor divisible by both 3 and 7")
        

# 5 leaf Year
year=int(input("Enter the Year : "))
if year%400==0 or year%4==0 and year% 100!=0 :
    print(year,"It is leaf year")
else :
    print(year,"it is not leaf year")

# 6. Check Pass or Fail (Passing marks = 35)
while True :
    num=int(input("Enter the Student marks :"))
    if num>=35 and num <100 :
        print(num ," \n Pass")
    elif num>100 :
        print(num,"\n Please Enter correct marks.")
    else :
        print(num,"\n Fail")

# 8. Check if character is vowel
       
while True :
    char=input("Enter the Character :").upper()
    if char in ['A','E','I','O','U'] :
        print(f"{char} is a vovel")
    else :
        print(f"{char} is not a vowel")

# 9. Check greatest of two numbers
    
while True :
    a=int(input("Enter the 1st number :")) # Enter the 1st number :9
    b=int(input("Enter the 2nd number :")) # Enter the 2nd number :7
    if a>b :
        print(a,"is greatest number.")
    else :
        print(b,"condition.py")
# output : 9 is greatest number.


# 10. Check smallest of two numbers
while True :
    a=int(input("Enter the 1st number :")) # Enter the 1st number :2
    b=int(input("Enter the 2nd number :")) # Enter the 2nd number :3
    if a<b :
        print(a,"is smaller number.")
    else :
        print(b,"is smaller number")
# output : 2 is smaller number.

# 11. Check if number is zero
while True :
    a=int(input("Enter the number :")) # Enter the number :0
    if a==0:
        print("Number is 0.")
    else :
        print("Number is not 0")
#output : Number is 0.

# 12. Check if number is multiple of 10

while True :
    num=int(input("Enter the number :")) # Enter the number :50
    if num%10==0:
        print(num,"is multiple of 10")
    else :
        print(num,"is not multiple of 10")
# output : 50 is multiple of 10



# 13. Check if age is eligible to vote (18+) Eligible to vote
age=int(input("Enter the your age :")) #Enter the your age :19

if age>=18 :
    print(f"{age}  is Eligible to vote")
else :
    print(f"{age}is not Eligible to vote")

# output :19  is Eligible to vote


# 14. Check if number is between 1 and 100
while True :
    num=int(input("Enter the number :")) # Enter the number :45

    if num>=1 and num<=100 :
        print(f"{num} is in range of between 1 and 100.")
    else :
        print(f"{num} id not in range of between 1 and 100.")
# output :45 is in range of between 1 and 100.


# 15. Check if number is square of another

num=int(input("Enter the number :")) # Enter the number :4
a=int(input("Enter the number a :")) # Enter the number a :2
if num==a**2 :
    print(f"{num} is square number.")
else :
    print(f"{num} is not a square number.") # output :4 is square number.


# 16. Check if two strings are equal
while True :
    str1=input("Enter the str1 :") # Enter the str1 :apple
    str2=input("Enter the str2 :") # Enter the str2 :apple
    if str1==str2 :
        print(f"Two strings are equal.")
    else :
        print(f"Two strings are not equal.") #output :Two strings are equal.




