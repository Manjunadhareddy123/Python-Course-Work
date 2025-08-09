# Instagram using oops conpect.

class Instagram :
    def __init__(self,username,password):
        print("Welcome to the instagram")
        self._bio=' '
        self.post=[]
        self.followers=[]
        self.following=[]
        self.username=username
        self.__password=password
        print(f"Hello {self.username} login successfull")

    @property
    def externalbio(self):
        return self._bio
    
    @externalbio.setter
    def externalbio(self,upd_bio):
        self._bio=upd_bio


    def showPassword(self):
        return self.__password
    def updatePassword(self,new_pwd):
        self.__password=new_pwd
manikanta=Instagram("manikanta","mani@1234!")

#public var accessing
print("Bio :",manikanta._bio)
print("Post :",manikanta.post)
print("Followers :",manikanta.followers)
print("Following :",manikanta.following)
print("Username :",manikanta.username)

# modifiying - public var

manikanta._bio='peace'
manikanta.post.append("python-course.png")
manikanta.followers.extend(['Adhitya','shanmuk','kiran'])
manikanta.following.extend(['jrntr','virat.kohli','klrahul'])
manikanta.username='manikanta_.'

print("\n After updating :")
print("Bio :",manikanta._bio)
print("Post :",manikanta.post)
print("Followers :",manikanta.followers)
print("Following :",manikanta.following)
print("Username :",manikanta.username)

# private var-accessing
print("\nPassword :",manikanta.showPassword())
print("update Password :",manikanta.updatePassword("mani@12"))


'''
Output :

Welcome to the instagram
Hello manikanta login successfull
Bio :  
Post : []
Followers : []
Following : []
Username : manikanta

 After updating :
Bio : peace
Post : ['python-course.png']
Followers : ['Adhitya', 'shanmuk', 'kiran']
Following : ['jrntr', 'virat.kohli', 'klrahul']
Username : manikanta_.

Password : mani@1234!
update Password : None
'''