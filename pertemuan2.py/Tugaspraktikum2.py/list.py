#python list
#List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

 #The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


#Access list items
#Biasanya indeks list dimulai dari 0:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#indeks negatif mulai dihitung dari elemen terakhir.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])    #-1 = elemen paling belakang
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:    #Untuk mengetahui apakah suatu item tertentu ada di dalam sebuah list, gunakan kata kunci in.
  print("Yes, 'apple' is in the fruits list")


# Change List Items  #mengganti nilai (isi) suatu elemen di dalam list
thislist = ["apple", "banana", "cherry"]  #menunjuk ke item kedua, yaitu "banana"
thislist[1] = "blackcurrant"  #nilai baru
print(thislist)

#Change a Range of Item Values     #mengganti beberapa item sekaligus di dalam list berdasarkan rentang index.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]   #thislist[1:2] → hanya "banana" Tapi diganti 2 item
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Insert Items  #insert() menambah tanpa menghapus
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#Add List Items
#Append Items  #append() digunakan untuk menambahkan satu item ke bagian paling belakang (akhir) list.
thislist = ["apple", "banana", "cherry"]   #orange" ditambahkan setelah "cherry"
thislist.append("orange")
print(thislist)

#Insert Items   #menambah item
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend List      #digunakan untuk menambahkan semua elemen dari list lain ke list yang sedang dipakai.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove List Items
#Remove Specified Item   #digunakan untuk menghapus item tertentu dari list berdasarkan NILAINYA, bukan berdasarkan index.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)   #pop() digunakan untuk menghapus item dari list berdasarkan INDEX (posisi).
print(thislist)

#Clear the List 
thislist = ["apple", "banana", "cherry"]
thislist.clear()   #clear() digunakan untuk menghapus SEMUA isi list.
print(thislist)


#Loop Lists
#Loop Through a List   #membaca isi list dari awal sampai akhir.
#thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

  #Loop Through the Index Numbers
  thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):   #len ()untuk tahu jumlah item    #range() → untuk bikin urutan index
  print(thislist[i])

#Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):   #Selain for, kita juga bisa mengulang isi list pakai while.
  print(thislist[i])
  i = i + 1

  #List Comprehension
#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#The Syntax
newlist = [x for x in fruits if x != "apple"]  #ondisi x != "apple" bernilai True untuk semua item selain "apple"
newlist = [x for x in fruits]

# Sort Lists
#Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()  #sort() digunakan untuk mengurutkan item di dalam list.
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)   #reverse=True → membalik urutan hasil sort
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)   #Fungsi key → mengembalikan angka/nilai pembanding
print(thislist)

#Copy Lists
#Use the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Use the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Use the slice Operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Join Lists
#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)