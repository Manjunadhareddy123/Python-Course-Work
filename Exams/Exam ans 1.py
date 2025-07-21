
# Q1)
date, month, year = input().split('-')
print(f"{year}/{month}/{date}")


'''
input :16-07-2025
output :2025/07/16
'''

# Q2)

num=int(input("Enter the Number :"))
if num%2==0 :
    print("Even Winner")
else :
    print("Odd Winner")

'''
Input :Enter the Number :22
Output :Even Winner

Input :Enter the Number :35
Output :Odd Winner

'''

#Q 3)
s=input().lower()
print(s.translate(str.maketrans('aeiou','*****')))
'''
Input :hello world
Output :h*ll* w*rld

Input :python is fun
Output :pyth*n *s f*n

'''



 # Q4)
marks = list(map(float, input("Enter marks: ").split()))
print(marks)
print(sum(marks))
print(max(marks))

'''
Input : Enter marks: 10.5 20.0 5.5 
[10.5, 20.0, 5.5]

Output :36.0
20.0
Input : Enter marks: 100.0 50.0
[100.0, 50.0]

Output:
150.0
100.0

'''

# Q5)
credentials=("admin","python123")
user=input()
password=input()
if credentials[0]==user and credentials[1]==password :
    print("Login Successful")
else :
    print("Access Denied")

'''
Input :admin    
python123
Output :Login Successful

Input :admin
wrongpass
Output :Access Denied


'''


# Q6)
names=input("Enter the Names(separated comma):").split(",")
name=set(names)
na=sorted(name)
print(na)
'''
Input :Enter the Names(separated comma):Asha,Ravi,Asha,Ravi,John
Output :['Asha', 'John', 'Ravi']
Input : Enter the Names(separated comma):Meena,Meena,Ravi
Output : ['Meena', 'Ravi']

'''
names=set(input().split(","))
print(sorted(names))
'''
Input :Ravi,Asha,Asha,John
Output :['Asha', 'John', 'Ravi']

Input :Meena,Arun,Arun,Ravi
Output :['Arun', 'Meena', 'Ravi']

'''

# 7)

n=int(input())
data={}
max_val=0
res_name=''
for _ in range(n):
    name,marks=input().split()
    marks=int(marks)
    if marks>max_val:
        max_val=marks
        res_name=name
        
    data[name]=marks

print(data)
print(res_name)

'''
Input :
3
Ravi 85
Anu 90
Sita 88

Output:
{'Ravi': 85, 'Anu': 90, 'Sita': 88}
Anu

Input :
2
Rahul 70
Meena 75
Output :
{'Rahul': 70, 'Meena': 75}
Meena


'''

# Q8)

sen=input().split()
for i in sen:
    print(i[::-1],end=' ')

'''
Input : hello world
Output :olleh dlrow 

Input :python is fun
Output :nohtyp si nuf 

'''


# Q9)
l=list(map(int,input().split()))
while(0 in l):
    l.remove(0)
print(l)

'''
Input :10 0 5 0 3
Output :[10, 5, 3]

Input : 0 0 1
Ouput :[1]

'''

# Q10 )
line=input()
data={}
for i in line:
    if i not in data and i!=' ':
        data[i]=line.count(i)
print(data)

'''
Input :hello world
Output :{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

Input :a b a
Output :{'a': 2, 'b': 1}

'''