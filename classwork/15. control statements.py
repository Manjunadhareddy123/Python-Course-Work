
n=int(input("Enter the size :"))
for row in range(n):
    for spc in range(row):
        print(" ",end=" ")
    for col in range(n-row) :
        print("*",end=" ")
    print()
'''
Input :Enter the size :13
Output :
* * * * * * * * * * * * * 
  * * * * * * * * * * * * 
    * * * * * * * * * * * 
      * * * * * * * * * * 
        * * * * * * * * * 
          * * * * * * * * 
            * * * * * * * 
              * * * * * *
                * * * * *
                  * * * *
                    * * *
                      * *
                        *



'''

n=int(input("Enter the size :"))
for row in range(n):
    print(" "*row,end=" ")
    print("*"*(n-row),end=" ")
    print()
'''
Input :Enter the size :10
Output :
 ********** 
  ********* 
   ******** 
    ******* 
     ****** 
      ***** 
       **** 
        *** 
         ** 
          * 

'''

n=int(input("Enter the size :"))
for row in range(n) :
    if row<=n//2 :
        print("*"*(row+1),end=" ")
    else :
        print('*'*(n-row),end="")
    print()

'''
Input :Enter the size :10
Output :
* 
**
***
****
*****
******
****
***
**
*
'''
#sqare
n=int(input("Enter the size (Square):"))
for row in range(n):
    for col in range(n) :
        if row==0 or row==n-1 or col==0 or col==n-1 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Input :Enter the size :5
Output :
* * * * * 
*       *
*       *
*       *
* * * * *
'''

# 8
n=int(input("Enter the size (8):"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1 or row==n//2 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Input :Enter the size :7
Output :
* * * * * * * 
*           *
*           *
* * * * * * *
*           *
*           *
* * * * * * *
'''
#

n=int(input("Enter the size (square):"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1 or row==n//2  or col==n//2:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Input : Enter the size :7
Output :
* * * * * * * 
*     *     *
*     *     *
* * * * * * *
*     *     *
*     *     *
* * * * * * *

'''
#square
n=int(input("Enter the size (Square):"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1 or col==n//2 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()

'''
Input :Enter the size :7
Output :
* * * * * * * 
*     *     *
*     *     *
*     *     *
*     *     *
*     *     *
* * * * * * *
'''

# Z
n=int(input("Enter the size(Z) :"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row+col==n :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''

'''
# X
n=int(input("Enter the size(X) :"))
for row in range(n):
    for col in range(n):
        if row==col  or row+col==n-1 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Input :Enter the size :10
Output:
*                 * 
  *             *
    *         *
      *     *
        * *
        * *
      *     *
    *         *
  *             *
*                 *
'''
    

n=int(input("Enter the size(X) :"))
for row in range(n):
    for col in range(n):
        if row==col  or row+col==n-1 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Input :Enter the size :10
Output:
*                 * 
  *             *
    *         *
      *     *
        * *
        * *
      *     *
    *         *
  *             *
*                 *
'''

# I
n=int(input("Enter the size(I) :"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==n//2:
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

# H
n=int(input("Enter the size (H):"))
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==n//2:
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

# S
n=int(input("Enter the size (S):"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row==n//2 or (col==0 and row<=n//2) or (col==n-1 and row>=n//2):
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Input :Enter the size :13
Output :
* * * * * * * * * * * * * 
*
*
*
*
*
* * * * * * * * * * * * *
                        *
                        *
                        *
                        *
                        *
* * * * * * * * * * * * *
'''

#A
n=int(input("Enter the size (A):"))
for row in range(n):
    for col in range(n):
        if row==0  or row==n//2  or col==0 or col==n-1:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Input : Enter the size :9
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

#M
n=int(input("Enter the size(M) :"))
for row in range(n):
    for col in range(n):
        if col==0  or col==n-1 or col==n//2 or row==0  :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()

'''
Input : Enter the size :9 
output :
* * * * * * * * * 
*       *       *
*       *       *
*       *       *
*       *       *
*       *       *
*       *       *
*       *       *
*       *       *
'''
