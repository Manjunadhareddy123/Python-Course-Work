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

#Dictionary Methods for Accessing Data

person = {'name' : 'Harshith', 'age' : 19}
print(person.get('name', 'Not Found')) # Output: Harshith
print(person.get('city', 'Unknown'))  # Output: Unknown


student = {'id': 101, 'name': 'Harshith', 'grade': 'A'}
print(student.keys())  # Output: dict_keys(['id', 'name', 'grade'])

print(student.values()) # Output: dict_values([101, 'Harshith', 'A'])

print(student.items())  # Output: dict_items([('id', 101), ('name', 'Harshith'), ('grade', 'A')])

#Dictionary Removing Data

info = {'name': 'Harshith', 'age': 25}
new_info = {'age': 19, 'city': 'Hyderabad'}
info.update(new_info)
print(info) # Output: {'name': 'Harshith', 'age': 19, 'city': 'Hyderabad'}


student = {'name': 'Anjali', 'course': 'Python'}
student.setdefault('age', 22)
print(student) # Output: {'name': 'Anjali', 'course': 'Python', 'age': 22}

#Dictionary Methods for Removing Data

person = {'name': 'Harshith', 'age': 19}
age = person.pop('age')
print(age)      # Output: 19
print(person)   # Output: {'name': 'Harshith'}

data = {'a': 1, 'b': 2, 'c': 3}
print(data.popitem())  # Output: ('c', 3)
print(data)   # Output: {'a': 1, 'b': 2}

info = {'name': 'Alex', 'city': 'Delhi'}
info.clear()
print(info)  # Output: {}

marks = {'math': 90, 'science': 85}
del marks['science']
print(marks)  # Output: {'math': 90}

#Built-in Functions for Dictionaries

data = {'a': 1, 'b': 2, 'c': 3}
print(len(data))  # Output: 3
empty_dict = {}
print(len(empty_dict))  # Output: 0

scores = {'math': 80, 'english': 70, 'science': 90}
print(max(scores))  # Output: science (based on alphabetical order)

scores = {'math': 80, 'english': 70, 'science': 90}
print(min(scores))  # Output: english

data = {'b': 2, 'a': 1, 'c': 3}
print(sorted(data))  # Output: ['a', 'b', 'c']

#Nested Dictionaries

students = {
"Harshith": {"age": 19, "course": "CS"},
"Doraemon": {"age": 22, "course": "Math"}
}
print(students["Harshith"]["course"]) # Output: CS

#Dictionary Comprehension

squares = {x: x*x for x in range(1, 6)}
print(squares) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#Count the Frequency of Words in a Sentence

sentence = "hello world hello python"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count) # Output: {'hello': 2, 'world': 1, 'python': 1}

#Find the Student with the Highest Marks

students = {
"Tekisuki": 85,
"Doraemon": 92,
"Nobita": 88
}
top_student = max(students, key=students.get)
print(top_student) # Output: Doraemon


