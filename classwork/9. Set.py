# 8 set

# create a set
s=set() # Empty set
print(s) # set()
s={1,2,3,4,5} # creating a set
print(s)# {1, 2, 3, 4, 5}
s={1,1,2,3,3,4,5,6,4,3,7} # duplicates are not allowed
print(s) # {1, 2, 3, 4, 5, 6, 7}

# 2. set Properties
s={1,2,3.5,4+6j,"manju",(1,2,3)} # diffirent data types
print(s) # {1, 2, 3.5, (4+6j), 'manju', (1, 2, 3)}
s.add(True)
s # {1, 2, 3.5, (4+6j), 'manju', (1, 2, 3)}
s.add("nadha")
print(s) # {1, 2, 3.5, (4+6j), 'manju', 'nadha', (1, 2, 3)}
# s.add([1,2,3]) # Syntax error

#3. Operation on set
# a. membership testing
#in
s={1,2,3,4,5}
print(s) #{1, 2, 3, 4, 5}
print(5 in s) # True
print(6 in s) # False
print(2 in s) # True

# not in
print(5 not in s) # False
print(7 not in s) # True
print(1 not in s) # False

# b.  Union (| or union() method) -->Returns the union of two sets
s1={1,2,3,4,5}
s2={3,4,5,6,7}
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {3, 4, 5, 6, 7}
print(s1 |s2) # {1, 2, 3, 4, 5, 6, 7}
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7}

# c.Intersection (& or intersection() method) --> Returns the intersection of two sets

print(s1 & s2) # {3, 4, 5}
print(s1.intersection(s2)) # {3, 4, 5}

# d. Difference (- or difference() method) -->Returns the difference between two sets
print(s1-s2) # {1, 2}
print(s1.difference(s2)) # {1, 2}

# e. Symmetric Difference (^ or symmetric_difference() method) --> Returns the symmetric difference between two sets

print(s1 ^ s2)# {1, 2, 6, 7}
print(s1.symmetric_difference(s2)) # {1, 2, 6, 7}

# f. Subset (<= or issubset() method)--> Returns True if the set is a subset of another set

s1={1,2,3,4,5}
print({2,3,4}<=s1) # True
print(s2<=s1) # False
print(s2<=s1) # False
print(s1<=s2 )# False
print(s1) # {1, 2, 3, 4, 5}
print(s2) # {3, 4, 5, 6, 7}
s2={2,3,4} 
print(s2<=s1 )# True
print(s1<=s2) # False

# g. Superset (>= or issuperset() method) --> Returns True if the set is a superset of another set


s3={1,2,3}
s4={2,3}
print(s3>=s2) # False
print(s3>=s4) # True
print(s3.issuperset(s4)) # True

# h. Disjoint Sets (isdisjoint() method) --> Returns True if two sets have no elements in common
s5={1,2,3,4,5}
s6={6,7,8,9}
print(s5.isdisjoint(s6)) # True
s7={1,2}
print(s5.isdisjoint(s7)) # False

# 4. Built-in Methods for Sets
s8={1,2,3,2.5,3.4,"manju",5,6,7}
print(s8) # {1, 2.5, 3.4, 2, 3, 5, 6, 7, 'manju'}

# add(element) --> Adds an element to the set 
print(s8.add(9))
print(s8.add("nadha"))
print(s8 )# {1, 2.5, 3.4, 2, 3, 5, 6, 7, 9, 'nadha', 'manju'}

# remove(element) -->  Removes an element; raises an error if the element doesn’t exist
print(s8.remove(3.4))
print(s8.remove(2))
print(s8) # {1, 2.5, 3, 5, 6, 7, 9, 'nadha', 'manju'}

# discard(element) --> Removes an element; does not raise an error if the element doesn’t exist

s8.discard(2)
s8 # {1, 2.5, 3, 5, 6, 7, 9, 'nadha', 'manju'}
s8.discard(2.5) 
s8 # {1, 3, 5, 6, 7, 9, 'nadha', 'manju'}

# pop() --> Removes and returns an arbitrary element

print(s8.pop()) # 1
print(s8.pop()) # 3

# clear() --> Removes all elements from the set
s9={1,2,3,4,6}
print(s9) # {1, 2, 3, 4, 6}
s9.clear()
print(s9) # set()

# update(other_set) --> Adds elements from another set to the current set
s9={1,2,3,4,6}
print(s9) # {1, 2, 3, 4, 6}
s9.update("manju")
s9.update("5")
print(s9) # {1, 2, 3, 4, 'j', 6, 'm', 'n', 'a', 'u', '5'}

# intersection_update(other_set) -->Updates the set with the intersection of itself and another set


s11={1,2,3,4,5}
s12={4,5,6,7,8}
print(s11) # {1, 2, 3, 4, 5}
print(s12 )# {4, 5, 6, 7, 8}
s11.intersection_update(s12)
print(s11) # {4, 5}
print(s12) # {4, 5, 6, 7, 8}
s12.difference_update(s11)
print(s12) # {6, 7, 8}
print(s12) # {6, 7, 8}

# symmetric_difference_update(other_set) --> Updates the set with the symmetric difference
 
s11={1,2,3,4,5}
s12={4,5,6,7,8}
print(s11) # {1, 2, 3, 4, 5}
print(s12) # {4, 5, 6, 7, 8}
s11.symmetric_difference_update(s12)
print(s11 )# {1, 2, 3, 6, 7, 8}

 # copy()--> Returns a shallow copy of the set
s13=s11.copy()
print(s13) # {1, 2, 3, 6, 7, 8}

# 5. Built-in Functions for Sets

s14={2,5,3,6,3,9,7,8}
print(s14)# {2, 3, 5, 6, 7, 8, 9}

print(len(s14)) # 7   len()
print(len({"manju"})) # 1 len()

print(min(s14) )# 2 min()

print(max(s14)) #  9 max()

print(sum(s14)) # 40 sum

print(sorted(s14)) # [2, 3, 5, 6, 7, 8, 9] # sorted

# set(iterable) --> Converts an iterable (e.g., list, string) to a set 
set([3,4,5,6]) #{3, 4, 5, 6}


# 6. Immutability and Frozensets

# Creating a frozenset
frozen = frozenset([1, 2, 3])
print(frozen)

# Frozenset is immutable
# The following will raise an error
# frozen.add(4)



