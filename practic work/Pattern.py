# A
n=int(input("Enter the Size :"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or col==n-1 or row==n//2 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Input :
Enter the Size :9

Output :
* * * * * * * * * 
*               * 
*               * 
*               * 
* * * * * * * * * 
*               * 
*               * 
*               * 
*               *
'''
# B
n=int(input("Enter the Size :"))
for row in range(n):
    for col in range(n) :
        if row==0 or row==n-1 or col==0 or col==n-1 or row==n//2 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Input :Enter the Size :9
Output :
* * * * * * * * *
*               *
*               *
*               *
* * * * * * * * *
*               *
*               *
*               *
* * * * * * * * *
'''
# C
n=int(input("Enter the Size :"))
for row in range(n):
    for col in range(n) :
        if row==0 or row==n-1 or col==0 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Input : Enter the Size :9
Output :
* * * * * * * * * 
*
*
*
*
*
*
*
* * * * * * * * *
'''
# E
n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row==n//2 or col==0 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()

'''
Input :Enter the size :9   
Output :                                                                               Enter the size :9
* * * * * * * * *
*
*
*
* * * * * * * * *
*
*
*
* * * * * * * * *
'''
# F
n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n//2 or col==0 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Input :Enter the size :9
Output :
* * * * * * * * * 
*
*
*
* * * * * * * * * 
*
*
*
*
'''
# H
n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==n//2 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Input :Enter the size :9
Output :
*               * 
*               * 
*               * 
*               * 
* * * * * * * * * 
*               * 
*               * 
*               * 
*               * 
'''
# I
n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==n//2 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Input :Enter the size :9
Output :
* * * * * * * * * 
        *
        *
        *
        *
        *
        *
        *
* * * * * * * * *
'''


# J
n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n):
        if row==0 or col==n//2 or (row==n-1 and col<n//2) : 
            print("*",end=" ")
        elif col==0 and row>n//2 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Input :Enter the size :9
Output :
* * * * * * * * * 
        *
        *
        *
        *
*       *
*       *
*       *
* * * * *
'''
# L
n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n):
        if row==n-1 or col==0:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()

'''
Input :Enter the size :9
Output :
*
*
*
*
*
*
*
*
* * * * * * * * *
'''
# K
n=int(input("Enter the size :"))
i=0
j=n//2+1
for row in range(n):
    for col in range(n):
        if col==0:
            print("*",end=" ")
            
        elif row==col+3 and col>1 :
              print("*",end=" ")
        elif  ((row==i and col==j) and col>0) :
              print("*",end=" ")
              i=i+1
              j=j-1

        else :
            print(" ",end=" ")
    print()
'''
Input : Enter the size :9
Output :
*         *       
*       *
*     *
*   *
* *
*   *
*     *
*       *
*         *
'''