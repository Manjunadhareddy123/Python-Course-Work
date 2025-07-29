
print("RED BUS TICKET BOOKING".center(100,"*"))
print("Passenger Details".center(75,"*"))
name=input("Enter the Name :")
age=int(input("Enter the Age :"))
gender=set(input("Enter the gender :").split())
mobile=int(input("Enter the Mobile Number :"))
email=input("Enter the Email id :")

print("Bus booking Details.".center(75,"*"))
Date=input("Enter the date(DD-MM-YYYY) :")
timings=input("Enter the timigs(HH:MM):")
starting_point=input("Enter the Strating point :")
ending_point=input("Enter the Ending point :")
bus_type=(input("Enter the bus type(AC / Non-AC): "))
travels=input("Enter the Travels name :")
picking_point=input("Enter the Picking point :")
droping_point=input("Enter the Dropint point :")

ticket_price=float(input("Enter the ticket price :"))

seat_type=(input("Enter seat type(Window/Aisle) :"))
seat_no=(input("Enter the seat number(Eg :u1,L1) :"))

food=input("Enter the Food include(Yes/No) :")
items_given=list(input("Items given(comma-separated):").split())

bus_no=input("Enter the Bus number (Eg :AA11,AB12):").upper()
bus_name=input("Enter the Bus name :").capitalize() 
print("Bus Driver Details".center(75,"*"))
driver_no=int(input("Enter the Driver number :"))
contact_no=int(input("Enter the Contact number :"))
driver_name=input("Enterthe Driver name :")

print("Your Details ".center(50,"*"))
print(f"passenger Name : {name}.")
print(f"passenger age : {age}.")
print("Gender :",gender)
print("Mobile Number :%d"%(mobile))
print("Email id %s:"%(email))
print("Date :",Date, "Timing :",timings)
print("Bus Details.".center(100,"-"))
print("Starting Point: {}, Ending Point : {}".format(starting_point,ending_point))
print(f"Bus Type:{bus_type}")
print(f"Travels Name :{travels}")
print(f"Picking point: {picking_point}, Droping point :{droping_point}")

print("Ticket Price :%d"%(ticket_price))
print(f"Seat Type:{seat_type},Seat number :{seat_no}")
print("food",food)
print(f"Item given :{items_given}")

print("Bus NUmber: {} ,Bus Name :{} ".format(bus_no,bus_name))

print("Driver Details".center(100,"-"))
print("Driver Name:{},Driver Number:{},contact Number:{}".format(driver_name,driver_no,contact_no))


''''
***************************************RED BUS TICKET BOOKING***************************************
*****************************Passenger Details*****************************
Enter the Name :Raja
Enter the Age :22
Enter the gender :Male
Enter the Mobile Number :9876543210
Enter the Email id :raja@gmail.com
****************************Bus booking Details.***************************
Enter the date(DD-MM-YYYY) :17-07-2025
Enter the timigs(HH:MM):22:21
Enter the Strating point :Kadapa
Enter the Ending point :Tirupati
Enter the bus type(AC / Non-AC): AC
Enter the Travels name :CGR
Enter the Picking point :Kadapa Bus stand
Enter the Dropint point :Tirupati Bus stand
Enter the ticket price :300.90
Enter seat type(Window/Aisle) :Window
Enter the seat number(Eg :u1,L1) :L1
Enter the Food include(Yes/No) :No
Items given(comma-separated):Water,Sweet,Pillow,Blanket
Enter the Bus number (Eg :AA11,AB12):AA11
Enter the Bus name :CGRA
*****************************Bus Driver Details****************************
Enter the Driver number :1231231231
Enter the Contact number :5674567567
Enterthe Driver name :ABC
-------------------------------------------Driver Details-------------------------------------------
Driver Name:ABC,Driver Number:1231231231,contact Number:5674567567


'''
