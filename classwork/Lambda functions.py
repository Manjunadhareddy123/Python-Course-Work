#lambda Functions
'''
syntax
var=lambda arg: exp 
var(arg)
'''
#Even or Odd
def evenorodd(n):
    if n%2==0:
        print(n,"is Even")
    else :
        print(n,"is Odd")
n=int(input("Enter the Number :"))
evenorodd(n)
'''
Enter the Number :14
14 is Even
'''
even_lambda=lambda n :"even" if n%2==0 else "odd"
print("even_lambda :",even_lambda(10))
print("Even lambda :",even_lambda(5))
'''
even_lambda : even
Even lambda : odd
'''


 # Square
def squares(s):
    print(s*s)
s=int(input("Enter the Number :"))
squares(s)
'''
Enter the Number :5
25
'''
def square(ss):
    for i in range(len(ss)):
        ss[i]**=2
    print(ss)
square([1,2,3,4,5])
'''
[1, 4, 9, 16, 25]
'''

n=6
square_lambda=lambda n:n*n
print("square_lambda :",square_lambda(n))
print("square_lambda :",square_lambda(7))
'''
square_lambda : 36
square_lambda : 49
'''

squa_lambda=list(map(lambda i:i*i ,[1,2,3,4,5,6]))
print("square lambda:",squa_lambda)
'''
square lambda: [1, 4, 9, 16, 25, 36]
'''

# Add
def add(a,b):
    return a+b
print(add(13,15))
print(add(100,202))
'''
28
302
'''
add_lambda=lambda a,b : a+b
print("Add_lambda :",add_lambda(4,5))
print("add_lambda :",add_lambda(10,15))
'''
Add_lambda : 9
add_lambda : 25
'''
add_lambda=list(map(lambda i:i+i,[1,2,3,4,5,6,7,8]))
print("add lambda :",add_lambda)
'''
add lambda : [2, 4, 6, 8, 10, 12, 14, 16]
'''

char_lambda=list(map(lambda i:i.upper(),'python'))
print("char lambda :",char_lambda)
'''
char lambda : ['P', 'Y', 'T', 'H', 'O', 'N']
'''

char_lambda=list(map(lambda i:ord(i),'python'))
print("char lambda :",char_lambda)
'''
char lambda : [112, 121, 116, 104, 111, 110]
'''
v='aeiou'
vowel_lambda=list(map(lambda i:'*' if i in v else i,'python'))
print("Vowel lambda:",vowel_lambda)
'''
Vowel lambda: ['p', 'y', 't', 'h', '*', 'n']
'''
v='aeiou'
vowel_lambda=list(map(lambda i:'*' if i in v else i,'python'))
print("Vowel lambda:",''.join(vowel_lambda))
'''
Vowel lambda: pyth*n
'''
data={'manju':55,'kowshik':65,'kiran':45,'ram':100}
sorted_data=dict(sorted(data.items(),key=lambda i:i[1]))
print(sorted_data)
'''
{'kiran': 45, 'manju': 55, 'kowshik': 65, 'ram': 100}
'''
data={'manju':55,'kowshik':65,'kiran':45,'ram':100}
sorted_data=dict(sorted(data.items(),key=lambda i:i[1],reverse=True))
print(sorted_data)
'''
{'ram': 100, 'kowshik': 65, 'manju': 55, 'kiran': 45}
'''
data={'manju':55,'kowshik':65,'kiran':45,'ram':100}
sorted_data=dict(sorted(data.items(),key=lambda i:i[0],reverse=True))
print(sorted_data)
'''
{'ram': 100, 'manju': 55, 'kowshik': 65, 'kiran': 45}
'''

maxnum=lambda a,b: a if a>b else b 
print(maxnum(34,56))
print(maxnum(79,54))
'''
56
79
'''

mulnum=lambda a,b: a*b
print(mulnum(2,10))
print(mulnum(3,15))
'''
20
45
'''
s=sorted({(1,3),(2,1),(4,2)},key=lambda i:i[1])
print(s)
'''
[(2, 1), (4, 2), (1, 3)]
'''
s=sorted({(1,3,5),(2,1,7),(4,2,1)},key=lambda i:i[2])
print(s)
'''
[(4, 2, 1), (1, 3, 5), (2, 1, 7)]
'''
l=[(1,3,5),(2,1,7),(4,2,1)]
s=sorted(l,key=lambda i:i[-1])
print(s)
'''
[(4, 2, 1), (1, 3, 5), (2, 1, 7)]
'''

l=["manju","nadha","reddy","kowshik","laddu"]
s=sorted(l,key=lambda i:i[2])
print(s)
'''
['nadha', 'reddy', 'laddu', 'manju', 'kowshik']
'''
l=["manju","nadha","reddy","kowshik","laddu"]
s=sorted(l,key=lambda i:i[-2])
print(s)
'''
['reddy', 'laddu', 'nadha', 'kowshik', 'manju']
'''

n=int(input("Enter the number :"))
evenorodd=lambda n: True if n%2==0 else False
print(evenorodd(n))
'''
Enter the number :55
False
Enter the number :20
True
'''
# List Indexing
l=[[23,34,23],[12,23,34],[34,45,63],[34,32,13],[34,45,67]]
print(sorted(l))
'''
output : [[12, 23, 34], [23, 34, 23], [34, 32, 13], [34, 45, 63], [34, 45, 67]]
'''

l=[[23,34,23],[12,23,34],[34,45,63],[34,32,13],[34,45,67]]
s=sorted(l,key=lambda i:i[-1])
print(s)
'''
Output :[[34, 32, 13], [23, 34, 23], [12, 23, 34], [34, 45, 63], [34, 45, 67]]
'''
# list in even numbers
l=[1,2,3,4,5,6,7,8,9,10]
e=list(filter(lambda i:i%2==0,l))
print(e)
'''
Output : [2, 4, 6, 8, 10]
'''
# list in odd numbers
l=[1,2,3,4,5,6,7,8,9,10]
e=list(filter(lambda i:i%2==1,l))
print(e)
'''
Output : [1, 3, 5, 7, 9]
'''
# filer using remove "0"
l=[1,2,0,0,4,7,5,0,0,0,3,2,4,2]
e=list(filter(lambda i:i!=0,l))
print(e)
'''
Output : [1, 2, 4, 7, 5, 3, 2, 4, 2]
'''

data={
    'laptopA':{'available':True,'price':40000},
    'laptopB':{'available':False,'price':35700},
    'laptopC':{'available':True,'price':45000},
    'laptopD':{'available':False,'price':60000},
    'laptopE':{'available':True,'price':80000},
    'laptopF':{'available':False,'price':70000},
    'laptopG':{'available':True,'price':50000},    
    'laptopH':{'available':False,'price':42000}
}

l=list(map(lambda i:i,data))
print(l)
'''
Output : ['laptopA', 'laptopB', 'laptopC', 'laptopD', 'laptopE', 'laptopF', 'laptopG', 'laptopH']

'''

data={
    'laptopA':{'available':True,'price':40000},
    'laptopB':{'available':False,'price':35700},
    'laptopC':{'available':True,'price':45000},
    'laptopD':{'available':False,'price':60000},
    'laptopE':{'available':True,'price':80000},
    'laptopF':{'available':False,'price':70000},
    'laptopG':{'available':True,'price':50000},    
    'laptopH':{'available':False,'price':42000}
}

l=list(map(lambda i:data[i],data))
print(l)
'''
Output :
[{'available': True, 'price': 40000}, {'available': False, 'price': 35700}, {'available': True, 'price': 45000}, {'available': False, 'price': 60000}, {'available': True, 'price': 80000}, {'available':
 False, 'price': 70000}, {'available': True, 'price': 50000}, {'available': False, 'price': 42000}]                                                                                                      
'''

# staus of labtops
data={
    'laptopA':{'available':True,'price':40000},
    'laptopB':{'available':False,'price':35700},
    'laptopC':{'available':True,'price':45000},
    'laptopD':{'available':False,'price':60000},
    'laptopE':{'available':True,'price':80000},
    'laptopF':{'available':False,'price':70000},
    'laptopG':{'available':True,'price':50000},    
    'laptopH':{'available':False,'price':42000}
}

l=list(map(lambda i:data[i]['available'],data))
print(l)
'''
Output : [True, False, True, False, True, False, True, False]

'''
# available Laptops
data={
    'laptopA':{'available':True,'price':40000},
    'laptopB':{'available':False,'price':35700},
    'laptopC':{'available':True,'price':45000},
    'laptopD':{'available':False,'price':60000},
    'laptopE':{'available':True,'price':80000},
    'laptopF':{'available':False,'price':70000},
    'laptopG':{'available':True,'price':50000},    
    'laptopH':{'available':False,'price':42000}
}

l=list(filter(lambda i:data[i]['available'],data))
print(l)
'''
Output : ['laptopA', 'laptopC', 'laptopE', 'laptopG']

'''
# Price below 50K 
data={
    'laptopA':{'available':True,'price':40000},
    'laptopB':{'available':False,'price':35700},
    'laptopC':{'available':True,'price':45000},
    'laptopD':{'available':False,'price':60000},
    'laptopE':{'available':True,'price':80000},
    'laptopF':{'available':False,'price':70000},
    'laptopG':{'available':True,'price':50000},    
    'laptopH':{'available':False,'price':42000}
}

l=list(filter(lambda i:data[i]['price']<50000,data))
print(l)
'''
Output :['laptopA', 'laptopB', 'laptopC', 'laptopH']
'''

# based on color balck
data={
    'laptopA':{'available':True,'price':40000,'color':'Green'},
    'laptopB':{'available':False,'price':35700,'color':'Black'},
    'laptopC':{'available':True,'price':45000,'color':'White'},
    'laptopD':{'available':False,'price':60000,'color':'Black'},
    'laptopE':{'available':True,'price':80000,'color':'Green'},
    'laptopF':{'available':False,'price':70000,'color':'Black'},
    'laptopG':{'available':True,'price':50000,'color':'Green'},    
    'laptopH':{'available':False,'price':42000,'color':'Black'}
}

l=list(filter(lambda i:data[i]['color']=='Black',data))
print(l)
'''
Output : ['laptopB', 'laptopD', 'laptopF', 'laptopH']
'''

# filter using even numbers

v=[1,2,3,4,5,6,7,8,9,10]
e=list(filter(lambda i:i%2==0,v))
print(e)
'''
Output : [2, 4, 6, 8, 10]

'''
# uppercase
v=['manju','nadha','reddy','kowshik']
s=list(map(lambda i :i.upper(),v))
print(s)
'''
Output: ['MANJU', 'NADHA', 'REDDY', 'KOWSHIK']
'''

# Title()
v=['manju','nadha','reddy','kowshik']
s=list(map(lambda i :i.title(),v))
print(s)
'''
Output :['Manju', 'Nadha', 'Reddy', 'Kowshik']

'''