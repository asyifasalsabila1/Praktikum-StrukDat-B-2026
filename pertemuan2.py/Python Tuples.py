#Tuple========================================
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
  
  #tuple item
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Tuple Length
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")   #String, int and boolean data types:
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
 
#The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets  
print(thistuple)

#type()
mytuple = ("apple", "banana", "cherry")       #<class 'tuple'>
print(type(mytuple))

#Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative  indexing
thistuple = ("apple", "banana", "cherry")         #-1 refers to the last item, -2 refers to the second last item etc.
print(thistuple[-1])
 
 #Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")       #This example returns the items from index -4 (included) to index -1 (excluded)    
print(thistuple[-4:-1])


