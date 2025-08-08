import sys
print(sys.argv)

# ['e:/codegnan/python course work/classwork/Built-in Modules.py'] 

print(sys.path)
'''
PS E:\codegnan\python course work> & C:/Users/lenovo/AppData/Local/Programs/Python/Python313/python.exe "e:/codegnan/python course work/classwork/Built-in Modules.py"
['e:\\codegnan\\python course work\\classwork', 'C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip', 'C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python313\\DLLs', 'C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python313\\Lib', 'C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python313', 'C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages']
'''

print(sys.version)
'''
C:/Users/lenovo/AppData/Local/Programs/Python/Python313/python.exe "e:/codegnan/python course work/classwork/Built-in Modules.py"
3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)]
PS E:\codegnan\python course work> '''

print(sys.exit)
'''
<built-in function exit>
'''

import platform
print(platform.system()) # Windows
print(platform.release()) # 11
print(platform.processor())# Intel64 Family 6 Model 140 Stepping 2, GenuineIntel

import math

print(math.pi) # 3.141592653589793
print(math.e) # 2.718281828459045
print(math.sqrt(25)) # 5.0
print(math.pow(2,3)) # 8.0
print(math.ceil(12.3)) # 13
print(math.ceil(12.8)) # 13
print(math.ceil(12.1)) # 13
print(math.floor(12.3)) # 12
print(math.floor(12.8)) # 12
print(math.floor(12.1)) # 12
print(math.fabs(-12)) # 12.0
print(abs(-12)) # 12
print(math.factorial(5)) # 120


print(math.gcd(12,24)) # 12
print(math.gcd(8,24)) # 8
print(math.gcd(8,12)) # 4
print(math.log(2)) # 0.6931471805599453
print(math.sin(45)) # 0.8509035245341184
print(math.cos(0)) # 1.0
print(math.tan(45)) # 1.6197751905438615
print(math.degrees(45)) # 2578.3100780887044
print(math.radians(30)) # 0.5235987755982988



import random


print(random.random()) # 0.8562221898843374
print(random.randint(1,6)) # 5
print(random.uniform(1,6)) # 2.158575152271515
names=['manju','kowshik','rasool','hemanth','laddu','siva']
print(random.choice(names)) # kowshik
print(random.choices(names,k=3)) # ['manju', 'rasool', 'siva']
print(random.shuffle(names)) # None


names=['manju','kowshik','rasool','hemanth','laddu','siva']
print(random.random()) # 0.4035406192791644
print(random.randint(1,6)) # 6
print(random.uniform(1,6)) # 4.0340608141528
names=['manju','kowshik','rasool','hemanth','laddu','siva']
print(random.choice(names)) # laddu
print(random.choices(names,k=3)) # ['laddu', 'manju', 'laddu']
print(random.shuffle(names)) # 
print(names) # ['rasool', 'kowshik', 'hemanth', 'laddu', 'siva', 'manju']

print(random.seed(2))
print(random.seed(2))
print(random.random()) # 
print(random.randint(1,6)) # 
print(random.uniform(1,6)) # 
names=['manju','kowshik','rasool','hemanth','laddu','siva']
print(random.choice(names)) # 
print(random.choices(names,k=3)) # 
print(random.shuffle(names)) # 


import random
import sys

def dice():
    return random.randint(1,6)

def first_player_turn():
    global player1_score
    player1_status=input(f"{player1}: Want to [C]ontinue or [S]top: ").upper()
    if player1_status=='C':
        player1_turn=dice()
        player1_score+=player1_turn
        if player1_score in snakes:
            player1_score=snakes[player1_score]
            print(f"\n{player1}'s turn:\nDice: {player1_turn}\n---Snake bite---\nBoard position: {player1_score}")
        elif player1_score in ladders:
            player1_score=ladders[player1_score]
            print(f"\n{player1}'s turn:\nDice: {player1_turn}\n*****Ladder*****\nBoard position: {player1_score}")
        else:
            print(f"\n{player1}'s turn:\nDice: {player1_turn}\nBoard position: {player1_score}")
    elif player1_status=='S':
        print(f'\n{player1} quit the game.\n{player2} Won the game!!!')
        sys.exit()

def second_player_turn():
    global player2_score   
    player2_status=input(f"{player2}: Want to [C]ontinue or [S]top: ").upper()
    if player2_status=='C':
        player2_turn=dice()
        player2_score+=player2_turn
        if player2_score in snakes:
            player2_score=snakes[player2_score]
            print(f"\n{player2}'s turn:\nDice: {player2_turn}\n---Snake bite---\nBoard position: {player2_score}")
        elif player2_score in ladders:
            player2_score=ladders[player2_score]
            print(f"\n{player2}'s turn:\nDice: {player2_turn}\n*****Ladder*****\nBoard position: {player2_score}")
        else:
            print(f"\n{player2}'s turn:\nDice: {player2_turn}\nBoard position: {player2_score}")
    elif player2_status=='S':
        print(f'\n{player2} quit the game.\n{player1} Won the game!!!')
        sys.exit()



player1=input("Enter the player-1: ")
player2=input("Enter the player-2: ")

player1_score=0
player2_score=0

winning_point=100

snakes={99:23,81:17,72:64,67:14,56:32,48:12,34:3,25:19,16:9}
ladders={7:19,18:77,23:85,31:44,45:71,54:63,61:94,78:88,89:93}


while player1_score<winning_point and player2_score<winning_point:
    first_player_turn()
    second_player_turn()        
else:
    if player1_score>player2_score:
        print(f"\n\n{player1} Win the game!!!!!!")
    elif player1_score==player2_score:
        print(f"\n\nTie!!!!!!")
    else:
        print(f"\n\n{player2} Win the game!!!!!!")

'''
Enter the player-1: manju
Enter the player-2: kowshik
manju: Want to [C]ontinue or [S]top: c

manju's turn:
Dice: 5
Board position: 5
kowshik: Want to [C]ontinue or [S]top: c

kowshik's turn:
Dice: 2
Board position: 2
manju: Want to [C]ontinue or [S]top: c

manju's turn:
Dice: 1
Board position: 6
kowshik: Want to [C]ontinue or [S]top: c

kowshik's turn:
Dice: 4
Board position: 6
manju: Want to [C]ontinue or [S]top: c

manju's turn:
Dice: 4
Board position: 10
kowshik: Want to [C]ontinue or [S]top: c

kowshik's turn:
Dice: 1
*****Ladder*****
Board position: 19
manju: Want to [C]ontinue or [S]top: c

manju's turn:
Dice: 5
Board position: 15
kowshik: Want to [C]ontinue or [S]top: c

kowshik's turn:
Dice: 3
Board position: 22
manju: Want to [C]ontinue or [S]top: c

manju's turn:
Dice: 3
*****Ladder*****
Board position: 77
kowshik: Want to [C]ontinue or [S]top: c

kowshik's turn:
Dice: 4
Board position: 26
manju: Want to [C]ontinue or [S]top: c

manju's turn:
Dice: 3
Board position: 80
kowshik: Want to [C]ontinue or [S]top: c

kowshik's turn:
Dice: 4
Board position: 30
manju: Want to [C]ontinue or [S]top: c

manju's turn:
Dice: 4
Board position: 84
kowshik: Want to [C]ontinue or [S]top: c

kowshik's turn:
Dice: 5
Board position: 35
manju: Want to [C]ontinue or [S]top: c

manju's turn:
Dice: 6
Board position: 90
kowshik: Want to [C]ontinue or [S]top: c

kowshik's turn:
Dice: 3
Board position: 38
manju: Want to [C]ontinue or [S]top: c

manju's turn:
Dice: 4
Board position: 94
kowshik: Want to [C]ontinue or [S]top: c

kowshik's turn:
Dice: 2
Board position: 40
manju: Want to [C]ontinue or [S]top: c

manju's turn:
Dice: 6
Board position: 100
kowshik: Want to [C]ontinue or [S]top: c

kowshik's turn:
Dice: 4
Board position: 44


manju Win the game!!!!!!
'''
    
##################################
'''
Enter the player-1: siva
Enter the player-2: laddu
siva: Want to [C]ontinue or [S]top: c

siva's turn:
Dice: 6
Board position: 6
laddu: Want to [C]ontinue or [S]top: c

laddu's turn:
Dice: 2
Board position: 2
siva: Want to [C]ontinue or [S]top: c

siva's turn:
Dice: 6
Board position: 12
laddu: Want to [C]ontinue or [S]top: c

laddu's turn:
Dice: 4
Board position: 6
siva: Want to [C]ontinue or [S]top: s

siva quit the game.
laddu Won the game!!!'''

