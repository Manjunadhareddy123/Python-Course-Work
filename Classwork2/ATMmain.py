import ATMlogin as atm

atm.welcome()

if atm.Login():
    while True :
        atm.Menu()
        ch=input("Enter the choice :").upper()
        if ch=='C':
            atm.Check_balance()
        elif ch=='D':
            atm.Deposit()
        elif ch=='W':
            atm.Withdraw()
        elif ch=='V':
            atm.View_transaction()
        elif ch=='E':
            print("Thankyou".center(50,'_'))
            break
        else :
            print("Invalid Choice")

'''
****************Welcome to the ATM****************
Enter the account number :12345
Enter the pin :123
Login Successful

 [C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit
Enter the choice :c

 Current Balance : 5678

 [C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit
Enter the choice :d
Enter the amount to deposit :1000
1000 is successfully desposited

 [C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit
Enter the choice :d
Enter the amount to deposit :3000
3000 is successfully desposited

 [C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit
Enter the choice :v
_______________Transactions History_______________
Deposited -$1000
Deposited -$3000
________________End of the history________________

 [C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit
Enter the choice :w
Enter the amount to withdraw :2000
$2000 is successfully Withdraw

 [C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit
Enter the choice :c

 Current Balance : 7678

 [C]heck Balance
[D]eposit
[W]ithdraw
[V]iew Transactions
[E]xit
Enter the choice :e
'''