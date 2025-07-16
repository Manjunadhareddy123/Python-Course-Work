# 2. Conditional statement
# 1. Check if a number is a 4-digit even number
while True :
    num=int(input("Enter the 4-digit  number :")) # Enter the 4-digit  number :2468
    if num % 2 ==0 :
        if num >=1000 and num <=9999 :
            print(f"{num} is 4-digit and even number.")
            break
        elif num <=-1000 and num >=-9999 :
            print(f"{num} is 4-digit and even number.")
            break
        else :
            print(f"{num} is 4-digit and not even number. ")
    else :
        print(f"{num} pleae check your number it's odd.")
        
# output : 2468 is 4-digit and even number.


# 2. Check if a character is a consonant
char1=input("Enter the character :").lower() # Enter the character :b
if char1 in ['a','e','i','o','u'] :
    print(f"{char1} is Consonant.")
else :
    print(f"{char1} is not Consonant.")

# output : b is not Consonant.

# 3. Check if a number is divisible by 2 or 3 but not both
while True :
    a=int(input("Enter the  number :"))  # Enter the  number :6

    if a%2==0 and a%3==0 :
        print(f"{a} is divisible by both 2 and 3.")
    elif a%2==0 and a%3 !=0 :
        print(f"{a} is divisible by 2 only.")
    elif a%3==0 and  a%2 !=0 :
        print(f"{a} is divisible by 3 only." )
    else :
        print(f"{a} is not divisible by both.")
'''

6 is divisible by both 2 and 3.
Enter the  number :4
4 is divisible by 2 only.
Enter the  number :9
9 is divisible by 3 only.
Enter the  number :11
11 is not divisible by both.'''

# 4. Check if a number is negative and odd 

num=int(input("Enter the number :"))  # Enter the number :-5
if num<0 and num%2==1 :
    print(f"{num} is Negative and odd number.")
elif num <0 and num%2==0 :
    print(f"{num} is Negative and not a odd number.")
elif num>0 and num%2==1 :
    print(f"{num} is positive and odd number.")
else :
    print(f"{num} is positive and no odd number.")

'''
output :
-5 is Negative and odd number.
Enter the number :-4
-4 is Negative and not a odd number.
Enter the number :5
5 is positive and odd number.
Enter the number :4
4 is positive and no odd number.'''


# 5. Check if a string starts with a vowel
str1=input("Enter the string :").lower() # Enter the string :apple
if len(str1) >0 :
    f_char=str1[0] 
    if f_char == 'a' or f_char == 'e' or f_char == 'i' or f_char == 'o' or f_char == 'u' :
        print(f"{str1} starts with a vowel.")
    else :
        print(f"{str1} not staerts with a vowel.")
else :
    print("nothing")

# output :apple starts with a vowel.

#6. Check if three sides form a valid triangle

a=int(input("Enter the 1st side length :")) # Enter the 1st side length :3
b=int(input("Enter the 2nd side length :")) # Enter the 2nd side length :4
c=int(input("Enter the 3rd side length :")) # Enter the 3rd side length :5

if a>0 and b>0 and c>0 :
    if a==3 :
        if b==4 and c==5 :
            print("valid triangle.")
        elif b==5 and c==4 :
            print("vaild triangle.")
        else :
            print("not Vaild triangle.")
    elif b==3 :
        if a==4 and c==5 :
            print("valid triangle.")
        elif a==5 and c==4 :
            print("vaild triangle.")
        else :
            print("not Vaild triangle.")

    elif c==3 :
        if a==4 and b==5 :
            print("valid triangle.")
        elif a==5 and b==4 :
            print("vaild triangle.")
        else :
            print("not Vaild triangle.")
else :
    print("not Vaild triangle. check once.")

# output : valid triangle.



# 7. Find the greatest among three numbers

a=int(input("Enter the 1st number :")) # Enter the 1st number :12
b=int(input("Enter the 2nd number :")) # Enter the 2nd number :45
c=int(input("Enter the 3rd Number :")) # Enter the 3rd Number :30

if a>b and a>c :
    print(f"{a} is the greatest number.")
elif b>a and b>c :
    print(f"{b} is the greatest number.")
else :
    print(f"{c} is the greatest number.")
# output : 45 is the greatest number.


# 8. Check if a year is a century year and leap year
year=int(input("Enter the year :")) # Enter the year :2004
if year%400==0 or year%4==0 and year%100==0 :
    print(f"{year} it is Century leap year.")
else :
    print(f"{year} it is not Century leaf year. ")
# output : 2000 it is leaf year.


#9. Check if a character is a digit

num=[0,1,2,3,4,5,6,7,8,9]
num1=int(input("Enter the number :")) # Enter the number :5
if num1 in num :
    print(f"{num1} is Digit.")
else :
    print(f"{num1} is not digit.")

# output : 5 is Digit.


# 11. Compare lengths of two strings

str1=input("Enter the 1st string :") # Enter the 1st string :cat
str2=input("Enter the 2nd string :") # Enter the 2nd string :mouse
a=len(str1)
b=len(str2)
if a>b:
    print(f"{str1} :first string is longer. ")
else :
    print(f"{str2} : second string is longer")

# output : mouse : second string is longer


# 12. Check if a number is within a specific range (50 to 100) and divisible by 5
num=int(input("Enter the number :")) # Enter the number :75
if num>=50 and num<=100 :
    if num % 5==0 :
        print(f"{num} in range and divisible  by 5.")
    else :
        print(f"{num} in range and not divisible bt 5.")
else :
    print(f"{num} is not in range and not divisible by 5.")

# output : 75 in range and divisible  by 5.

#13. Validate if a password length is strong (8 or more characters)

pwd=input("Enter the passwor : ") # Enter the password : secure123
a=len(pwd)
if a>=8:
    print(f"{pwd} is Strong password.")
else :
    print(f"{pwd} is not strong password.")

# output : secure123 is Strong password.

#14. Check if sum of two numbers is even

num1=int(input("Enter the 1st number :")) # Enter the 1st number :12
num2=int(input("Enter the 2nd number :")) # Enter the 2nd number :16
num3=num1+num2
if num3 % 2==0 :
    print("Sum is even")
else :
    print("Sum is odd")

# output : Sum is even


# 15. Check if the character is a special symbol (!, @, #, etc.)

list1=['!','@','#','$','%','^','&','*','(',')','-','_','=','+','\',','{','}', ';',':',',','/','?','.','>','¢','°','€']
char1=input("Enter the charcter :") # Enter the charcter :@
if char1 in list1 :
    print(f"{char1} is special charcter.")
else :
    print(f"{char1} is not special charcter.")

# output : @ is special charcter.

# 16. Check if temperature is cold (<15°C), moderate (15–30°C), or hot (>30°C)

temp=int(input("Enter the Temperature :")) # Enter the Temperature :10
if temp > 0 and temp< 100:
    if temp <15 :
        print(f"{temp}°C cold.")
    elif temp>=15 and temp <=30 :
        print(f"{temp}°C moderate.")
    else :
        print(f"{temp}°C hot")
else :
    print("check your input.")

# output : 10°C cold.


# 17. Check if a number lies outside the range 10 to 50
num=int(input("Enter the number :")) # Enter the number :55
if num<10 :
    if num>=10 and num>=50 :
        print(f"{num} inside the range.")
    else :
        print(f"{num} outside the range.")
else :
    print(f"{num} is outside range.")

# output : 55 is outside range.


# 18. Check if number is a perfect square (basic method)

num = int(input("Enter a number: ")) # Enter a number: 36
i = 1
found = False
while i * i <= num:
    if i * i == num:
        found = True
        break
    i += 1
if found:
    print(f"{num} Perfect square")
else:
    print(f"{num} Not a perfect square")

# output : 36 Perfect square

# 19. Compare two ages and determine who is older or if same age


num1=int(input("Enter the 1st person age :")) # Enter the 1st person age :22
num2=int(input("Enter the 2nd person age :")) # Enter the 2nd person age :25

if num1 > num2 :
    print(f"{num1}  first person is older.")
elif num1<num2 :
        print(f"{num2} ,second person is older.")
else :
    print("same age.")

# output :25,second person is older.


# 20. Check if an angle is acute, right, or obtuse

angle=int(input("Enter the adgle in degrees :")) # Enter the adgle in degrees :90
if angle >0 and angle <90 :
    print("Acute angle")
elif angle==90 :
    print("right angle")
elif angle >90 and angle <180 :
    print("obtuse angle")
else :
    print("Invaild angle.")

#output : right angle





