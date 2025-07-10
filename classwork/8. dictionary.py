# Dict

# 1. Introduction to Dictionary


# Syntax of a Dictionary:
# dictionary_name = {key1: value1, key2: value2, key3: value3}

# Example of a Dictionary:

student={
    "Roll no" : 1,
    "Nmane" : " Manju",
    "branch" : "CSE"
    }
    
print(student) # {'Roll no': 1, 'Nmane': ' Manju', 'branch': 'CSE'}


# 2. Dictionary Operations

# 2.1 Accessing Values

d1={"name":"abc","age":21,"gender" : "male","branch":"CSE"}   
d1 # {'name': 'abc', 'age': 21, 'gender': 'male', 'branch': 'CSE'}
print(d1["name"]) # abc
print(d1["branch"]) # CSE

# 2.2 Adding and Updating Items
d1={"name":"abc","age":21,"gender" : "male","branch":"CSE"}
d1["Location"]="kadapa"
d1["Roll no"]=1

# 2.3 Removing Items from a Dictionary

# pop --> Removes the specified key and returns its value.
print(d1) # {'name': 'abc', 'age': 21, 'gender': 'male', 'branch': 'CSE', 'Location': 'kadapa', 'Roll no': 1}
d1.pop("Roll no") # 1
d1.pop("Location") # 'kadapa'

# del --> Deletes a specific key-value pair or the entire dictionary.

del d1['age']
print(d1) # {'name': 'abc', 'gender': 'male', 'branch': 'CSE'}

# popitem --> Removes and returns the last inserted key-value pair.
d1.popitem()
('branch', 'CSE')
print(d1) # {'name': 'abc', 'gender': 'male'}

# clear() --> Removes all key-value pairs, making the dictionary empty.

d1.clear()
print(d1) #{}

d2={'name': 'abc', 'age': 21, 'gender': 'male', 'branch': 'CSE', 'Location': 'kadapa', 'Roll no': 1}
print(d2)
{'name': 'abc', 'age': 21, 'gender': 'male', 'branch': 'CSE', 'Location': 'kadapa', 'Roll no': 1}

# 3. Dictionary Built-in Methods

# 3.1 Dictionary Methods for Accessing Data #eva
eval



