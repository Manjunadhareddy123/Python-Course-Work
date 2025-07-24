# Q1) Automated Salary Tax Calculator
salary=int(input("Enter the salary :"))
if 0<salary<=250000 :
    print("NO TAX")
elif 250001<= salary <=500000 :
    print(salary*0.05)
elif 500001<= salary <=1000000 :
    print(salary * 0.2)
elif salary >1000000 :
    print(salary * 0.3)

'''
Enter the salary :300000
15000.0
Enter the salary :1000000
200000.0
'''

# Q2) Movie Ticket Pricing System

n=int(input("Enter the Number :"))
total=0
for i in range(n):
    age=int(input("Enter the age :"))
    if 0 < age <=5 :
        pass
    elif 5< age <=18 :
        total+=100
    elif 19<= age <=60 :
        total+=150
    elif age>60 :
        total+=120
print(total)
'''
Enter the Number :4
Enter the age :3
Enter the age :17
Enter the age :36
Enter the age :65
370
'''
# Q3) Electricity Bill Generator
units=int(input("Enter the units :"))
if 0< units <=100 :
    print(units * 1.5)
elif 101<= units <=200 :
    print((100* 1.5)+((units-100 )*2.5))
elif 201<= units <=500 :
    print((100*1.5)+(100*2.5)+((units-200 )* 4))
elif units<500 :
    print((100*1.5)+(100*2.5)+(300*4.5)+((units-500 )* 6))

'''
Enter the units :250
600.0
'''
# Q4) Car Parking Fee Calculator
hr=int(input("Enter the Hours :"))
if hr==2 :
    print("30")
elif 2< hr <24 :
    print(30+((hr-2)*10))
elif hr==24 :
    print("200")
'''
Enter the Hours :2
30
Enter the Hours :3
40
Enter the Hours :24
200

'''
# 5) Product Inventory Checker (Nested Conditionals)
product_name=input("Enter the Product Name :")
stock=int(input("Enter the stock :"))
if stock==0:
    print(f"{product_name}: Out of Stock")
elif 1<= stock <=10 :
    print(f"{product_name}: Low Stock")
elif 11 <= stock <= 50 :
    print(f"{product_name}: In Stock ")
elif stock>50 :
    print(f"{product_name}: Overstocke")

'''
Enter the Product Name :mouse
Enter the stock :5
mouse: Low Stock

'''
# Q6) Pattern – Row-wise Alternating 0 and 1 (Nested Loops)
n=int(input("Enter the size :"))
for row in range(n):
    for col in range(n):
        print((row+col)%2,end=" ")
    print()
'''
Enter the size :5
0 1 0 1 0 
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
'''
# Q7) Gym Subscription Billing (Menu Driven Program)
while True:
    print("""1. Monthly – ₹500 
2. Quarterly – ₹1300 
3. Yearly – ₹5000
0.Exit
""")
    ch=int(input("Enter the choice :"))
    if ch==0:
        break
    people=int(input("Enter the number of people :"))
    if ch==1:
        print(500 * people)
    elif ch==2:
        print(1300 * people)
    elif ch==3 :
        print(5000 * people)
    else :
        print("INvalid details.")
'''
1. Monthly – ₹500 
2. Quarterly – ₹1300
3. Yearly – ₹5000
0.Exit

Enter the choice :1
Enter the number of people :5
2500
1. Monthly – ₹500
2. Quarterly – ₹1300
3. Yearly – ₹5000
0.Exit

Enter the choice :2
Enter the number of people :3
3900
1. Monthly – ₹500
2. Quarterly – ₹1300
3. Yearly – ₹5000
0.Exit

Enter the choice :3
Enter the number of people :3
15000
1. Monthly – ₹500
2. Quarterly – ₹1300
3. Yearly – ₹5000
0.Exit

Enter the choice :0

'''
# 8) Billing Bot – Apply Discount Based on Amount
amount=float(input("Enter the amount :"))
discount=0
if 0 < amount <=999 :
    pass
elif 1000 <= amount <= 4999 :
    discount=amount * 0.05
elif 5000 <= amount <= 9999 :
    discount=amount * 0.1
elif amount >=10000 :
    discount=amount * 0.15
print(amount-discount)
'''
Enter the amount :12000
10200.0

'''
# Q9) ATM PIN Verification with Blocking Logic
stored_pin='1234'
for i in range(3):
    pin=input("Enter the Pin :")
    if stored_pin==pin :
        print("Access Granted")
        break
else :
    print("ATM Blocked. Try Again Later.")
'''
pra22.py                                                                                      Enter the Pin :1222
Enter the Pin :1234
Access Granted

Enter the Pin :1111
Enter the Pin :1222
Enter the Pin :1232
ATM Blocked. Try Again Later.

'''

# Q 10) Bus Booking System – Track Full and Empty Seats
total_seats=int(input("Enter the Total Seats :"))
booked_seats=input("Enter the booked Seats :").split()
print(f"Total Seats: {total_seats}")
print(f"Booked Seats :{len(booked_seats)}")
print(f"Available Seats :{total_seats-len(booked_seats)}")
'''
Enter the Total Seats :40
Enter the booked Seats :1 2 5 4 6 12 15 32 44
Total Seats: 40
Booked Seats :9
Available Seats :31

'''