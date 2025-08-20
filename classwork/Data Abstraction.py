from abc import ABC, abstractmethod

class Bankaccount(ABC):
    def deposit(self):
        print("You can deposit amount")
    def checkbalance(self):
        print("You can check your balance")

    @abstractmethod
    def withdraw(self):
        pass

    def viewhistory(self):
        print("You can check the history")

class CurrentAccount(Bankaccount):
    def withdraw(self):
        print("You can withdraw Extra amount also")

class SavingAccount(Bankaccount):
    def withdraw(self):
        print("You can wiothdraw the amount ")

mani=CurrentAccount()
shanmukh=SavingAccount()

mani.checkbalance()
mani.deposit()
mani.withdraw()
mani.viewhistory()

print("\n shamukh")

shanmukh.checkbalance()
shanmukh.deposit()
shanmukh.withdraw()
shanmukh.viewhistory()
'''
You can check your balance
You can deposit amount
You can withdraw Extra amount also
You can check the history

 shamukh
You can check your balance
You can deposit amount
You can wiothdraw the amount 
You can check the history
'''