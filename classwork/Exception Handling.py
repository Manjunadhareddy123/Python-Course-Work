try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[2]
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number :"))
    print(b)
    c=1+"1"

except NameError :
    print("a is not define")
except IndexError :
    print("You have entered the put of range value")

except KeyError :
    print("Key is not present")

except ValueError :
    print("Enter the proper data type")

except TypeError :
    print("You can't add 2 diff types")

'''
4
Enter a number :3
3
You can't add 2 diff types
'''

# NameError
try:
    a=a+10
except NameError :
    print("a is not define")
'''
a is not define
'''

# IndexError
try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[5]
except NameError :
    print("a is not define")
except IndexError :
    print("You have entered the put of range value")

'''
You have entered the put of range value
'''

# KeyError
try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[1]
    d={1:2,2:4,3:9}
    print(d[4])

except NameError :
    print("a is not define")
except IndexError :
    print("You have entered the put of range value")
except KeyError :
    print("Key is not present")
'''
Key is not present
'''

#  ValueError
try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[1]
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number :"))
    print(b)

except NameError :
    print("a is not define")
except IndexError :
    print("You have entered the put of range value")
except KeyError :
    print("Key is not present")
except ValueError :
    print("Enter the proper data type")
'''
Enter the proper data type
'''


# TypeError
try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[2]
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number :"))
    print(b)
    c=1+"1"

except NameError :
    print("a is not define")
except IndexError :
    print("You have entered the put of range value")

except KeyError :
    print("Key is not present")

except ValueError :
    print("Enter the proper data type")

except TypeError :
    print("You can't add 2 diff types")

'''
4
Enter a number :4
4
You can't add 2 diff types
'''

# to reduce the code of lines just mention the all type of erroes
try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[2]
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number :"))
    print(b)
    c=1+"12"

except (NameError, IndexError, KeyError, ValueError, TypeError) as e :
    print(f"Error occured : {e}")

'''
4
Enter a number :5
5
Error occured : unsupported operand type(s) for +: 'int' and 'str'
'''

#  Exception key was used to reduce more.
try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[5] #
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number :"))
    print(b)
    c=1+"12"

except Exception as e :
    print(f"Error occured : {e}")

'''
Error occured : list index out of range.
'''

# In Exception used else statement the code will be correct.
try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[2] #
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number :"))
    print(b)
    c=1+12

except Exception as e :
    print(f"Error occured : {e}")

else :
    print("No errors")
    print(c)

'''
4
Enter a number :4
4
No errors
13
'''

#  Exception Handling  Finally
try:
    a=10
    a=a+10
    l=[1,2,3]
    k=l[2] #
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number :"))
    print(b)
    c=1+12

except Exception as e :
    print(f"Error occured : {e}")

else :
    print("No errors")
    print(c)

finally :
    print("Code executed")

'''
4
Enter a number :13
13
No errors
13
Code executed
'''
#  Exception Handling
try:
    amount = int(input("Enter the amount :"))
    if amount < 0 :
        raise ValueError("Enter the positive value")

except Exception as e :
    print(f"Error occured : {e}")

else :
    print("No errors")
    print("You can withdraw")

finally :
    print("------------------- Remove your card -------------------------")


'''
Enter the amount :5000
No errors
You can withdraw
------------------- Remove your card -------------------------


Enter the amount :-3000
Error occured : Enter the positive value
------------------- Remove your card -------------------------
'''