data={
    1:{"product name":"Rice" ,"price":60},
    2:{"product name":"Wheat Floar" ,"price":45},
    3:{"product name":"Sugur" ,"price":160},
    4:{"product name":"Milk" ,"price":30},
    5:{"product name":"Eggs" ,"price":40},
    6:{"product name":"Cooking Oil" ,"price":200},
    7:{"product name":"Tea Power" ,"price":130},
    8:{"product name":"Salt" ,"price":90},
    9:{"product name": "Bread","price":20},
    10:{"product name":"Soap" ,"price":25}

}
for i in data :
    print(f"{i}.\t{data[i]["product name"]} -\t ${data[i]["price"]}")

items=list(map(int,input("Enter the product indexes(1,2,3,4) :").split()))
total=0
s=set()
for i in items :
    if i not in s :
        c=items.count(i)
        print(f"{data[i]["product name"]}-{c}*${data[i]["price"]}=${c*data[i]["price"]}")
        total+=data[i]["price"]*c
        s.add(i)
print(f"Total Bill {total}")

'''
Input :
1.      Rice -   $60
2.      Wheat Floar -    $45
3.      Sugur -  $160
4.      Milk -   $30
5.      Eggs -   $40
6.      Cooking Oil -    $200
7.      Tea Power -      $130
8.      Salt -   $90
9.      Bread -  $20
10.     Soap -   $25
Enter the product indexes(1,2,3,4) :1 1 1 2 3 5 5 4 6 6 7 7

Output :
Rice-3*$60=$180
Wheat Floar-1*$45=$45
Sugur-1*$160=$160
Eggs-2*$40=$80
Milk-1*$30=$30
Cooking Oil-2*$200=$400
Tea Power-2*$130=$260
Total Bill 1155


'''



print("Photo Gallery")
data1={
    1:{"name":"beach.jpg"},
    2:{"name":"mountain.jpg"},
    3:{"name":"party1.jpg"},
    4:{"name":"selfie.jpg"},
    5:{"name":"birthday.jpg"},
    6:{"name":"concert.jpg"},
    7:{"name":"sunset.jpg"},
    8:{"name":"trip.jpg"}
}
for i in data1 :
    print(f"{i}.\t{data1[i]["name"]}")

items=list(map(int,input("Select photos to share (enter numbers separated by comma)\n Your Selection :").split(",")))

s=set()
for i in items :
    if i not in  s:
        print(f"{data1[i]["name"]}")
        s.add(i)
print()

'''
Input :
Photo Gallery
1.      beach.jpg
2.      mountain.jpg
3.      party1.jpg
4.      selfie.jpg
5.      birthday.jpg
6.      concert.jpg
7.      sunset.jpg
8.      trip.jpg

Output :
Select photos to share (enter numbers separated by comma)
 Your Selection :1,1,2,2,3,4,5,5,6,7,8,8
beach.jpg
mountain.jpg
party1.jpg
party1.jpg
selfie.jpg
birthday.jpg
concert.jpg
sunset.jpg
party1.jpg

'''

total=0
data={
    'milk':30,
    'bread':50,
    'sugur':40,
    'oil':20
}
print(data)
while True :
    product_name=input("Enter the product name(0-Exit) :")
    if product_name=='0':
        print("Thank You")
        break
    quantity=int(input("Enter the quantity :"))
    total += data[product_name] * quantity
print(total)

'''
Input :
{'milk': 30, 'bread': 50, 'sugur': 40, 'oil': 20}
Enter the product name(0-Exit) :milk
Enter the quantity :3
Enter the product name(0-Exit) :bread
Enter the quantity :2
Enter the product name(0-Exit) :oil
Enter the quantity :2
Enter the product name(0-Exit) :0

Output :

Thank You
230
'''
print("Photo Gallery")
data1={
    1:"beach.jpg",
    2:"mountain.jpg",
    3:"party1.jpg",
    4:"selfile.jpg",
    5:"birthday.jpg",
    6:"concert.jpg",
    7:"sunset.jpg",
    8:"trip.jpg"
}
for i in data1:
    print(f"{i}.{data1[i]}")
li=set(map(int,input("Enter the indexes:").split(",")))
for i in li :
    print(f"{data1[i]}-shared")

'''
Photo Gallery
1.beach.jpg
2.mountain.jpg
3.party1.jpg
4.selfile.jpg
5.birthday.jpg
6.concert.jpg
7.sunset.jpg
8.trip.jpg

Input :Enter the indexes:2,2,2,1,4,5,3,8,7,6,3,4,5
Output :
beach.jpg-shared
mountain.jpg-shared
party1.jpg-shared
selfile.jpg-shared
birthday.jpg-shared
concert.jpg-shared
sunset.jpg-shared
trip.jpg-shared
'''