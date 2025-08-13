data={'current_balance':25000,'history':[]}
def check_balance():
    print(f"Current Blance :{data['current_balance']}")
def deposit():
    amount=int(input("Enter the amount :"))
    data['current_balance']+=amount
    data['history'].append(f"Deposited - ${amount}")
    print(f"Deposited Successfully - ${amount}")

def withdraw():
    amount=int(input("Enter the amount :"))
    if data['current_balance']>=amount:
        data['current_balance']-=amount
        data['history'].append(f"withdraw - ${amount}")
        print(f"Withdraw Successfully - ${amount}")
    else :
        print("Ins blnc")
def history():
    print("Transactions")
    for i in data['history']:
        print(i)

while True :
    print("Welcome to ATM".center(50,'*'))
    print('1.Check Balance')
    print('2.Deposit')
    print('3.withdraw')
    print('4.History')
    print('0.Exit')

    op=int(input("Enter Your choice :"))
    if op==0:
        print("Thank you".center(50,"="))
        break
    elif op==1:
        check_balance()
    elif op==2:
        deposit()
    elif op==3:
        withdraw()
    elif op==4:
        history()
    else:
        print("Invalid choice.Try Again.")


'''
******************Welcome to ATM******************
1.Check Balance
2.Deposit
3.withdraw
4.History
0.Exit
Enter Your choice :1
Current Blance :25000
******************Welcome to ATM******************
1.Check Balance
2.Deposit
3.withdraw
4.History
0.Exit
Enter Your choice :2
Enter the amount :5000
Deposited Successfully - $5000
******************Welcome to ATM******************
1.Check Balance
2.Deposit
3.withdraw
4.History
0.Exit
Enter Your choice :3
Enter the amount :2000
Withdraw Successfully - $2000
******************Welcome to ATM******************
1.Check Balance
2.Deposit
3.withdraw
4.History
0.Exit
Enter Your choice :4
Transactions
Deposited - $5000
withdraw - $2000
******************Welcome to ATM******************
1.Check Balance
2.Deposit
3.withdraw
4.History
0.Exit
Enter Your choice :1
Current Blance :28000
******************Welcome to ATM******************
1.Check Balance
2.Deposit
3.withdraw
4.History
0.Exit
Enter Your choice :0
====================Thank you=====================
'''