
# Polymorphism
# 2. Method Overriding (Run-Time Polymorphism)

class NormalUser :
    def __init__(self,username):
        self.username=username
        print(f"\nWelcome to Youtube \n{self.username} account is created")

    def playvideo(self):
        print("Ads Included")
        print("No background play")
        print("Limited content")
        print("Download with low Quality")
        print("No YT Music")
    
    def profile(self):
        print("You can upload your profile")
    def MultipleDevice(self):
        print("You can login with different devices")
    def shorts(self):
        print("You can see the YT Shorts")
    def Likes(self):
        print("Likes")
    def Comments(self):
        print("Comments")
    def Share(self):
        print("Share")
    def Subscribe(self):
        print("Subscribe")


class PermiumUser(NormalUser):
    def __init__(self,username):
        super().__init__(username)

    def playvideo(self):
        print("Ads Free")
        print("You can play on Background")
        print("Exclusive Content")
        print("Download with High quality")
        print("YT jMusic is avaiilable")


raju=NormalUser("Raju")
raju.playvideo()
raju.profile()
raju.MultipleDevice()
raju.shorts()
raju.Likes()
raju.Comments()
raju.Share()
raju.Subscribe()

manju=PermiumUser("Manju")
manju.playvideo()
manju.profile()
manju.MultipleDevice()
manju.shorts()
manju.Likes()
manju.Comments()
manju.Share()
manju.Subscribe()


'''

Welcome to Youtube 
Raju account is created
Ads Included
No background play
Limited content
Download with low Quality
No YT Music
You can upload your profile
You can login with different devices
You can see the YT Shorts
Likes
Comments
Share
Subscribe

Welcome to Youtube
Manju account is created
Ads Free
You can play on Background
Exclusive Content
Download with High quality
YT jMusic is avaiilable
You can upload your profile
You can login with different devices
You can see the YT Shorts
Likes
Comments
Share
Subscribe
'''


# Operator Overloading

class Number :
    def __init__(self,number):
        self.number=number

    def __add__(self,other):
        return self.number + other.number
    
    def __sub__(self,other):
        return self.number - other.number
    
    def __mul__(self,other):
        return self.number * other.number
    
    def __truediv__(self,other):
        return self.number / other.number
    
    def __eq__(self,other):
        return self.number == other.number
    
    def __gt__(self,other):
        return self.number > other.number
    
    def __lt__(self,other):
        return self.number < other.number
    
 
    def __nt__(self,other):
        return self.number != other.number

n1=Number(20)
n2=Number(10)

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n2/n1)
print(n1==n2)
print(n1>n2)
print(n1<n2)
print(n1 != n2)

'''
Output :

30
10
200
0.5
False
True
False
True
'''

