#Login page using OOPS Conpect.

import random

class Login:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._otp=random.randint(1111,9999)


    def getpassword(self):
        return self.__password
    
    def updatepassword(self,new_pwd):
        self.__password=new_pwd

    @property
    def publicotp(self):
        return self._otp
    
    @publicotp.setter
    def publicotp(self,new_otp):
        self._otp=new_otp
    
manju=Login("manjunadha","manju@123")

#public
print("password :",manju.username)

#private
print("Password :",manju.getpassword())

# protected
print("OTP :",manju.publicotp)

manju.username="_manju_"
print("Updated username :",manju.username)

manju.updatepassword("ma@123")
print("Updated password,:",manju.getpassword())

#manju.publicotp=
#print("Updated otp :",manju.publicotp)
print("Updated OTP :",manju.publicotp)
'''
Output :

password : manjunadha
Password : manju@123
OTP : 1234
Updated username : _manju_
Updated password,: ma@123
Updated OTP : 6493
'''