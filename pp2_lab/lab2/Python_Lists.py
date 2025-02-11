#Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 
  
  
  
#Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



#Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 

#
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) 

#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)



#list
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)


list1 = ["abc", 34, True, 40, "male"]
print(list1)


#type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#the list() constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)



#Loop Through A list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 
  
#Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
#Using a while Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
#Looping using list Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 



#Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
del thislist 

#Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)



#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 

#
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) 

#The syntax: condition
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)

#
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)


#Iterable
newlist = [x for x in range(10)]

print(newlist)

#
newlist = [x for x in range(10) if x < 5]

print(newlist)

#Expression
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

#
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)

#
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)



#Sort Lists Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Customze sort function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) 

#list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)



#Join two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) 

#
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) 



#list Methods
#append()
a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.append(b)

print(a)


#clear()
fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)


#copy()
fruits = ["apple", "banana", "cherry"]

x = fruits.copy()

print(x)


#count()
fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)


#extend()
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)


#index()
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)


#insert()
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)


#pop()
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)


#remove()
fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)


#reverse()
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)


#sort()
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)
