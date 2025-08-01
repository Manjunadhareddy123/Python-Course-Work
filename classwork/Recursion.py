# 1 to n numbers

n=int(input("Enter the Numbyer :"))
for i in range(1,n+1):
    print(i,end=" ")
'''
Enter the Numbyer :10
1 2 3 4 5 6 7 8 9 10 
'''

def update(n):
    if n==0 :
        return 
    print("Before :",n)
    update(n-1)
    print("Aftetr :",n)

n=int(input("Enter the number :"))
print(update(n))

'''
Explaintion
update(8)=
8 = update(7)==8
7=>update(6)=7
6=>update(5)=6
5=update(4)=5
4=update(3)=4
3=update(2)=3
2=update(1)=2
1=update(0)=1
'''



'''
Enter the number :10
Before : 10
Before : 9
Before : 8
Before : 7
Before : 6
Before : 5
Before : 4
Before : 3
Before : 2
Before : 1
Aftetr : 1
Aftetr : 2
Aftetr : 3
Aftetr : 4
Aftetr : 5
Aftetr : 6
Aftetr : 7
Aftetr : 8
Aftetr : 9
Aftetr : 10
None
'''

# sum of N numbers
def sumofnums(n):
    if n==0 :
        return n
    return n+sumofnums(n-1)
print(sumofnums(8))
'''
Explation
sumofnums(8)=36
8+sumofnums(7)=8+28=36
7+sumofnums(6)=7+21=28
6+sumofnums(5)=6+15=21
5+sumofnums(4)=5+10=15
4+sumofnums(3)=4+6=10
3+sumofnums(2)=3+3=6
2+sumofnums(1)=2+1=3
1+sumofnums(0)=1+0=1
'''

'''
36
'''

# Factorial
def factorial(n):
    if n==1:
        return n
    return n*factorial(n-1)
print(factorial(8))
print(factorial(10))
print(factorial(5))
'''
40320
3628800
120
'''

# Reverse String.
def reverse(s,ind):
    if ind==len(s):
        return
    reverse(s,ind+1)
    print(s[ind],end=" ")

s="python programming"
reverse(s,0)
'''
Explation:

reverse(s,0)=p
reverse(s,1)=y
reverse(s,2)=t
reverse(s,3)=h
reverse(s,4)=o
reverse(s,5)=n
reverse(s,6)=' '
reverse(s,7)=p
reverse(s,8)=r
reverse(s,9)=o
reverse(s,10)=g
reverse(s,11)=r
reverse(s,12)=a
reverse(s,13)=m
reverse(s,14)=m
reverse(s,15)=i
reverse(s,16)=n
reverse(s,17)=g
reverse(s,18)=stop
'''

'''
g n i m m a r g o r p   n o h t y p 
''' 
#Sum of Digits
def  sumofdigit(n):
    if n==0:
        return 0
    return(n%10)+sumofdigit(n//10)
print(sumofdigit(2345678))

'''
Explaition :

34567%10=7=> 34567//10=3456
3456%10=6=> 3456//10=345
345%10=5=> 345//10=34
34%10=4=>34//10=3
3%10=3=>3//10=0
'''
'''
35
'''