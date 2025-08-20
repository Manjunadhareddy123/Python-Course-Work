# 1. Square of a number using lambda
n=int(input("Enter the number :"))
square=lambda n:n**2
print(square(n))
'''
Enter the number :12
144

'''
# 2. Check if number is even using lambda
n=int(input("Enter the number :"))
evenorodd=lambda n: True if n%2==0 else False
print(evenorodd(n))
'''
Enter the number :55
False
Enter the number :20
True
'''

# 3. Get maximum of two numbers using lambda
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
evenorodd=lambda a,b :a if a>b else b
print(evenorodd(a,b))
'''
Enter the number :5
Enter the number :4
5

Enter the number :2
Enter the number :3
3

'''
# 4. Multiply two numbers using lambda
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
multiply=lambda a,b :a*b
print(multiply(a,b))
'''
Enter the first number :15
Enter the second number :10
150
'''
# 5.1. Sort a list of tuples by second element in reverse order using lambda
l=[(1, 3), (2, 1), (4, 2)]
sorted1=sorted(l,key=lambda i:i[1],reverse=True)
print(sorted1)
'''
[(1, 3), (4, 2), (2, 1)]
'''
# 5.2. Sort a list of tuples by second element  and reverse order using lambda
l=[(1, 3), (2, 1), (4, 2)]
sorted1=sorted(l,key=lambda i:i[-1],reverse=True)
print(sorted1)
'''
[(1, 3), (4, 2), (2, 1)]
'''
# 5.3. Sort a list of tuples by second element using lambda
l=[(1, 3), (2, 1), (4, 2)]
sorted1=sorted(l,key=lambda i:i[1])
print(sorted1)
'''
[(2, 1), (4, 2), (1, 3)]
'''
# 5.4. Sort a list of tuples by first  element using lambda
l=[(1, 3), (2, 1), (4, 2)]
sorted1=sorted(l,key=lambda i:i[0])
print(sorted1)
'''
[(1, 3), (2, 1), (4, 2)]
'''
# 6. Filter even numbers from a list using lambda and filter()
l=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda i : i%2==0,l)))
'''
[2, 4, 6, 8, 10]
'''
# 6. Filter Odd numbers from a list using lambda and filter()
l=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda i : i%2==1,l)))
'''
[1, 3, 5, 7, 9]

'''
# 7. Square each element in a list using lambda and map()
l=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda i :i*i,l)))
'''
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
# 8.1. Convert list of strings to uppercase using lambda
l=['manju','kowshik','laddu']
print(list(map(lambda i : i.upper(),l)))
'''
['MANJU', 'KOWSHIK', 'LADDU']
'''
#  8.2. Convert list of strings to lowercase using lambda
l=['MANJU', 'KOWSHIK', 'LADDU']
print(list(map(lambda i : i.lower(),l)))
'''
['manju', 'kowshik', 'laddu']
'''



