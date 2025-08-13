data={
    12345:{'pin':123,'balance':5678,'history':[]},
    23456:{'pin':123,'balance':5678,'history':[]},
    34567:{'pin':123,'balance':5678,'history':[]},
    45678:{'pin':123,'balance':5678,'history':[]},
    56789:{'pin':123,'balance':5678,'history':[]},
    67890:{'pin':123,'balance':5678,'history':[]}
    }
acc_num=None
login_status=None

def welcome():
    print("Welcome to the ATM".center(50,'*'))

def Menu():
    print('\n [C]heck Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transactions')
    print('[E]xit')

def Login():
    account_number=int(input("Enter the account number :"))
    pin=int(input("Enter the pin :"))
    global acc_num
    global login_status
    if account_number in data :
        if data[account_number]['pin']==pin:
            print("Login Successful")
            acc_num=account_number
            login_status=True
            return True
        else :
            print("Invaild pin")
            login_status=False

            return False
        
    else :
        print("Invalid account number")
        login_status=False
        return False

def Check_balance():
    if login_status and acc_num :
        print(f'\n Current Balance : {data[acc_num]["balance"]}')
    else :
        print("You need to login again")

def Deposit():
    if login_status and acc_num:
        amount=int(input("Enter the amount to deposit :"))
        data[acc_num]['balance']+=amount
        data[acc_num]['history'].append(f'Deposited -${amount}')
        print(f'{amount} is successfully desposited')
    else :
        print("You need to login again")

def Withdraw():
    if login_status and acc_num :
        amount=int(input("Enter the amount to withdraw :"))
        if data[acc_num]['balance']>=amount:
            data[acc_num]['balance']-=amount
            data[acc_num]['history'].append(f'Withdraw - ${amount}')
            print(f'${amount} is successfully Withdraw')
        else :
            print("Insufficient Balance")
    else:
        print("You need to login again")

def View_transaction():
    if login_status and acc_num :
        if data[acc_num]['history']:
            print("Transactions History".center(50,'_'))
            for i in data[acc_num]['history']:
                print(i)
            else :
                print("End of the history".center(50,'_'))
        else :
            print("No Transactions")
    else :
        print("You need to login again")


