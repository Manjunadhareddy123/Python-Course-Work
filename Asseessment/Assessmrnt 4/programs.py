def EvenorOdd():
    print('''
    Program:
    ----------------------------------------------------
    number = int(input("Enter the Number: "))
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")

    Test Cases:
    ----------------------------------------------------
    Enter the Number: 12
    12 is Even

    Enter the Number: 13
    13 is Odd

    Explanation:
    ----------------------------------------------------
    he program takes an integer input from the user. It checks if the number is divisible by 2 using the modulus operator (%). If divisible (i.e., number % 2 == 0), it prints "Even", otherwise, it prints "Odd".
    ''')
    


def factorial():
    print('''
    Program:
    ----------------------------------------------------
    n = int(input("Enter the number: "))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial of", n, "is", fact)

    Test Cases:
    ----------------------------------------------------
    Enter the number: 5
    Factorial of 5 is 120

    Enter the number: 6
    Factorial of 6 is 720

    Explanation:
    ----------------------------------------------------
    The program calculates the factorial of a given number by multiplying all integers from 1 to that number. It uses a for loop to iteratively multiply the numbers and stores the result in the variable fact, which is then printed
    ''')

def diamand_pattern():
    print('''
          
    Program :
    ----------------------------------------------------------
    # Diamond Pattern
    n=int(input("Enter the size :"))
    for row in range(n) :
        print(" "*(n-row-1)+'* '*(row+1))
    for row in range(n-2,-1,-1) :
        print(" "*(n-row-1)+'* '*(row+1))
    print()
          
    Output :
    ------------------------------------------------------
    Input :Enter the size :5
              * 
             * * 
            * * * 
           * * * * 
          * * * * * 
           * * * * 
            * * *
             * *
              *
    
          
    Explanation :
    ----------------------------------------      
    The program prints a diamond pattern by increasing stars in the first half and decreasing in the second half, with spaces to center-align the stars.

    ''')

def PositiveorNegative():
    print('''
     program :
    -----------------------------------------------     

    num=5 
    if num>0 :
        print("Positive Number")
    elif num< 0:
        print("Negative number")
    else :
        print("Zero")

    Output :
    ----------------------------------------------
    Negative number
          
    
    Explanation :
    ---------------------------------------------  
    num is 5, which is greater than 0, so the first if condition is true.
    The program prints "Positive Number" and skips the other conditions.

    ''')

def leaf_year():
    print('''
     program :
    -----------------------------------------------     

    year=2024 
    if year%400==0 or year%4==0 and year% 100!=0 :
        print(year,"It is leaf year")
    else :
        print(year,"it is not leaf year")

    Output :
    ----------------------------------------------
    2024 It is leaf year
    
    Explanation :
    ---------------------------------------------  
    2024 is divisible by 4 but not by 100, so the leap year condition is true.
    The program prints "2024 It is leaf year".

    ''')
    
def Check_if_number_is_zero():
    print('''
     program :
    -----------------------------------------------     

    a=0
    if a==0:
        print("Number is 0.")
    else :
        print("Number is not 0")

    Output :
    ----------------------------------------------
    Number is 0.
    
    Explanation :
    ---------------------------------------------  
    Since a is 0, the condition a == 0 evaluates to true.
    The program executes the first print statement and outputs "Number is 0.".

    ''')

def Eligible_to_vote():
     print('''
     program :
    -----------------------------------------------     

    age=19

    if age>=18 :
        print(f"{age}  is Eligible to vote")
    else :
        print(f"{age}is not Eligible to vote")

    Output :
    ----------------------------------------------
    19  is Eligible to vote
          
    
    Explanation :
    ---------------------------------------------  
    ince age is 19, the condition age >= 18 is true.
    The program prints "19 is Eligible to vote"

    ''')
     
def Check_if_temperature_is_hot_30():
    print('''
     program :
    -----------------------------------------------     

    temperature =35
    if temperature >30 :
        print(f"{temperature}°C it's hot.")
    else :
        print(f"{temperature}°Cit's not hot.")

    Output :
    ----------------------------------------------
    35°C it's hot.
          
    
    Explanation :
    ---------------------------------------------  
    Since temperature is 35, the condition temperature > 30 is true.
    The program prints "35°C it's hot.".
    ''')

def passorfail():
    print('''
     program :
    -----------------------------------------------     

    num=40
    if num>=35 and num <100 :
        print(num ," \n Pass")
    elif num>100 :
        print(num,"\n Please Enter correct marks.")
    else :
        print(num,"\n Fail")

    Output :
    ----------------------------------------------
    40  Pass
          
    
    Explanation :
    ---------------------------------------------  
    Since num is 40, it satisfies num >= 35 and num < 100, making the first condition true.
    The program prints "40 Pass".

    ''')
def greatest_number():
    print('''
     program :
    -----------------------------------------------     
    a=9
    b=7
    if a>b :
        print(a,"is greatest number.")
    else :
        print(b," greatest number.")
   

    Output :
    ----------------------------------------------
    9 is greatest number.
          
    
    Explanation :
    ---------------------------------------------  
    Since a (9) is greater than b (7), the condition a > b is true.
    The program prints "9 is greatest number."

    ''')

