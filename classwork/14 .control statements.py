
for row in range(5) :
    for col in range(5) :
        print("*",end=" ")
    print()
'''
# Output

* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

'''


for row in range(5) :
    for col in range(5) :
        print(row,end=" ")
    print()
'''
output :
0 0 0 0 0 
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
'''

for row in range(5) :
    for col in range(5) :
        print(col,end=" ")
    print()
'''
Output :
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
'''

for row in range(5) :
    for col in range(row+1):
        print(row,end=" ")
    print()
'''
Output :
0 
1 1 
2 2 2
3 3 3 3
4 4 4 4 4

'''
n=int(input("Enter the size :"))
for row in range(n) :
    for col in range(row+1):
        print(row,end=" ")
    print()
'''
Input :Enter the size :10
Output :
0 
1 1
2 2 2
3 3 3 3
4 4 4 4 4
5 5 5 5 5 5
6 6 6 6 6 6 6
7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9

'''


n=int(input("Enter the size :"))
for row in range(n) :
    for col in range(n-row):
        print("#",end=" ")
    print()
'''
Input :Enter the size :8
Output :
# # # # # # # # 
# # # # # # #
# # # # # #
# # # # #
# # # #
# # #
# #
#

'''

n=int(input("Enter the size :"))
for row in range(n) :
    for spa in range(n-row-1):
        print(" ",end=" ")
    for col in range(row+1):
        print("*",end=" ")
    print()
'''
Input :    Enter the size :10
Ouput :
                  * 
                * *
              * * *
            * * * *
          * * * * *
        * * * * * *
      * * * * * * *
    * * * * * * * *
  * * * * * * * * *
* * * * * * * * * *
'''
'''
n=int(input("Enter the size :"))
for row in range(n):
    print(" ",(n-row-1),end= " ")
'''