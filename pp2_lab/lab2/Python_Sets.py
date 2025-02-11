#Set
thisset = {"apple", "banana", "cherry"}
print(thisset) 


#Duplicates not Allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#Get the length of a set
thisset = {"apple", "banana", "cherry"}

print(len(thisset)) 

#Set Items - Data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False} 

#
set1 = {"abc", 34, True, 40, "male"}

print(set1)


#type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

#set()
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 



#Access set items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 
  
#
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) 

#
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset) 



#Add set Items
#Add items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) 

#Add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Add any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) 



#Remove set items
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset) 

#
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset) 

#
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset) 

#
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset) 

#
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) 



#Loop sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 
  
  

#Join sets
#Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 

#
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3) 

#Join Multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) 

#
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset) 

#Join a set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z) 

#Update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) 

#Intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3) 

#
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1) 

#
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

#Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3) 

#
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3) 

#
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1) 

#Symmetric Differences
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) 

#
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3) 

#
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1) 



#Set Methods
#add()
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits) 

#clear()
fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits) 

#copy()
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)

#difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z) 

#difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x) 

#discard()
fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits) 

#intersection()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z) 

#intersection_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x) 

#isdisjoint()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z) 

#issubset()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z) 

#issuperset()
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z) 

#pop()
fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits) 

#remove()
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits) 

#symmetric_difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z) 

#symmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#union()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z) 

#update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x) 