# Conditional Statements
'''
# simple if
if condition :
    # if-true statement

# if-else #
if condition :
    # if-true statement
else:
    # if-true statement

#if elif-else 
if condition :
    # if-true statement
elif condition-2:
    # if-true statement
    # elif condition-3:
    # if-true statement


elif condition-n:
    # if-true statement
else :
    #flase


    
 # Nested if
if condition-outer:
    if condition-ineer:
        # if-true stms
    else:
        # if-true stms
else:
    #flase statement.
    #  
#------------------- 
while True :
    s=input("Enter the status(R O G):")
    if s=='R':
        print("Stop")
    if s=='O':
        print("Ready")
    if s=='G':
        print("GO")
    
while True:
    items=['shoes','smartwatch','phone','laptop','airprods','toycar']

    print("Welcome to Amazon store".center(50,'*'))
    searchinput=input("Enter the item :").lower()

    if searchinput in items :
        print(f"{searchinput} found.Buy now !!!")
    else :
        print(f"{searchinput} is out of stock now.We will notify you.")


while True :
    s=input("Enter the status (L N):").upper()
    if s=='L':
        print("Do not talk")
    if s=='N' :
        print("Talk")


# Weekend Budget Plan
while True :
    amount=int(input("Enter the amount you can spend for weekend :"))
    if amount > 20000 :
        print("Trip to Goa")
    elif amount > 15000 :
        print("Go for Shopping")
    elif amount >10000 :
        print("Clubling")
    elif amount >5000 :
        print("Cafe /Dinner")
    elif amount >2000 :
        print("Maintances")
    elif amount >500 :
        print("Go for Movie")
    elif amount > 100 :
        print("Go for Street Food")
    else :
        print("go to home sleep and get some dreams.")

'''
while True :
    data={
        1:{'name':'manju','attempt':True,'python':80,'sql':90,'powerbi':75},
        2:{'name':'kowshik','attempt':True,'python':99,'sql':90,'powerbi':65},
        3:{'name':'siva','attempt':False,'python':0,'sql':0,'powerbi':0},
        4:{'name':'koti kiran','attempt':True,'python':60,'sql':70,'powerbi':85},
        5:{'name':'teja','attempt':False,'python':0,'sql':0,'powerbi':0}
    }
    stuid=int(input("Enter the student id : "))
    if data[stuid]['attempt']:
        total=(data[stuid]['python']+data[stuid]['sql']+data[stuid]['powerbi'])/3
        if total > 90 :
            print(f'Congrates !!! \n {data[stuid]["name"]} got "A" grade')
        elif total >75 :
             print(f'Good !!! \n {data[stuid]["name"]} got "B" grade')
        elif total >50 :
            print(f'Try to improve !!! \n {data[stuid]["name"]} got "C" grade')
        elif total >35 :
            print(f'Just Passed !!! \n {data[stuid]["name"]} got "D" grade')
        else :
            print(f'Better luck next Time !!! \n {data[stuid]["name"]} Failed')
    else :
        print(f'{data[stuid]["name"]} is not attempted the exam.')
