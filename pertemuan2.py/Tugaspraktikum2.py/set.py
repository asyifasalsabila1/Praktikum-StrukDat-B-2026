# Sets
myset = {"apple", "banana", "cherry"}
thisset = {"apple", "banana", "cherry"}
print(thisset)
#Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#Access Set Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

#Add Set Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Remove Set Items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#Loop Sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

  #Join Sets
  set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)
#Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

#frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
