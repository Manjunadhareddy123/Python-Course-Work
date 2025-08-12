#Single Inheritance
class A:
    def display_a(self):
        print("Parents class A")   
class B:
    def display_b(self):
        print("Child class B<-A") 
a=A()
a.display_a()              
b=B()
b.display_b()                
a.display_a() 
'''
Parents class A
Child class B<-A
Parents class A
'''

#2. Inheritance=multiple parents and only one child
class A:
    def display_a(self):
        print("Parent class A")   
class B:
    def display_b(self):
        print("parent class B") 
class C:
    def display_c(self):
        print("Parent class C")  
class D(A,B,C):
    def display_d(self):
        print("Child class A,B,C->D")
d=D()
d.display_a()                     
d.display_b()                     
d.display_c()                     
d.display_d()   
'''
Parent class A
parent class B
Parent class C
Child class A,B,C->D
'''

# 3.Multilevel Inheritance
class A:
    def display_a(self):
        print("Parent class A")   
class B(A):
    def display_b(self):
        print("parent class B") 
class C(B):
    def display_c(self):
        print("Parent class C")  
class D(C):
    def display_d(self):
        print("Child class A,B,C->D")
d=D()
d.display_a()                     
d.display_b()   
d.display_c()
d.display_d()   
'''
Parent class A
parent class B
Parent class C
Child class A,B,C->D
'''

# 4 Hierarchical Inheritance=Multiple subclasses inherit from a single superclass.
class A:
    def display_a(self):
        print("Parent class A")   
class B(A):
    def display_b(self):
        print("parent class B") 
class C(A):
    def display_c(self):
        print("Parent class C")  
class D(A):
    def display_d(self):
        print("Child class A,B,C->D")
b=B()
b.display_a()   
b.display_b()

c=C()
c.display_a() 
c.display_c() 

d=D()
d.display_a()
d.display_d()
'''
Parent class A
parent class B
Parent class A
Parent class C
Parent class A
Child class A,B,C->D
'''

# Whatapp status Upadtes of versions
class Status2015:
    def view(self):
        print("You can view status.")
    def reply(self):
        print("You can reply.")
    def caption(self):
        print("You can add caption.")
    
class Status2020(Status2015):
    def uploadImg(self):
        print("You can upload Image.")
    def uploadVid(self):
        print("You can upload video - 30 sec.")
    def privacy(self):
        print("You can select who can see your status.")

class Status2023(Status2020):
    def ProfilePrivacy(self):
        print("You can update the profile privacy.")
    def reaction(self):
        print("You can send reactions.")
    def like(self):
        print("You can like the Status.")

class Status2024(Status2020):
    def statusrings(self):
        print("Color is added to the status display.")
    def mute(self):
        print("You can mute the other's status.")
    def filters(self):
        print("You can filters.")

class Status2025(Status2023,Status2024):
    def music(self):
        print("Yoe can add music.")
    def mention(self):
        print("You can mention them.")
    def collab(self):
        print("You can share your status from insta or fb.")
    def voicenote(self):
        print("You can voice note.")

print("\n Siva")
siva=Status2015()
siva.view()
siva.reply()
siva.caption()

print("\nRavi")
ravi=Status2020()
ravi.uploadImg()
ravi.uploadVid()
ravi.privacy()
ravi.view()
ravi.reply()
ravi.caption()

print("\nKowshik")
Kowshik=Status2023()
Kowshik.uploadImg()
Kowshik.uploadVid()
Kowshik.privacy()
Kowshik.view()
Kowshik.reply()
Kowshik.caption()
Kowshik.ProfilePrivacy()
Kowshik.reaction()
Kowshik.like()

print("\nTarit")
tarit=Status2024()
tarit.uploadImg()
tarit.uploadVid()
tarit.privacy()
tarit.view()
tarit.reply()
tarit.caption()
tarit.statusrings()
tarit.mute()
tarit.filters()

print('\nmanju')
manju=Status2025()
manju.uploadImg()
manju.uploadVid()
manju.privacy()
manju.view()
manju.reply()
manju.caption()
manju.statusrings()
manju.mute()
manju.filters()
manju.ProfilePrivacy()
manju.reaction()
manju.like()

'''
You can view status.
You can reply.
You can add caption.

Ravi
You can upload Image.
You can upload video - 30 sec.
You can select who can see your status.
You can view status.
You can reply.
You can add caption.

Kowshik
You can upload Image.
You can upload video - 30 sec.
You can select who can see your status.
You can view status.
You can reply.
You can add caption.
You can update the profile privacy.
You can send reactions.
You can like the Status.

Tarit
You can upload Image.
You can upload video - 30 sec.
You can select who can see your status.
You can view status.
You can reply.
You can add caption.
Color is added to the status display.
You can mute the other's status.
You can filters.

manju
You can upload Image.
You can upload video - 30 sec.
You can select who can see your status.
You can view status.
You can reply.
You can add caption.
Color is added to the status display.
You can mute the other's status.
You can filters.
You can update the profile privacy.
You can send reactions.
You can like the Status.
'''

