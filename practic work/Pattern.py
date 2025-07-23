
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

# Diamond Pattern
n=int(input("Enter the size :"))
for row in range(n) :
    print(" "*(n-row-1)+'* '*(row+1))
for row in range(n-2,-1,-1) :
    print(" "*(n-row-1)+'* '*(row+1))
print()

'''
Input :Enter the size :5
Output :
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * *
   * *
    *

'''
# 6. Number Triangle

n=int(input("Enter the size :"))
for row in range(n) :
    for col in range(row+1):
        print(col,end=" ")
    print()

'''
Input :Enter the size :5
Output :
0 
0 1
0 1 2
0 1 2 3
0 1 2 3 4
'''


# 7. Floyd’s Triangle

n=int(input("Enter the size :"))
num=1
for row in range(1,n+1) :
    for col in range(row):
        print(num,end=" ")
        num+=1
    print()
'''
Input :Enter the size :5
Output :
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''

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
Input :Enter the size(Z) :9
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