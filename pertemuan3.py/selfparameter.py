'''
Parameter tersebut selfmerupakan referensi ke instance kelas saat ini.

Ini digunakan untuk mengakses properti dan metode yang dimiliki oleh kelas tersebut.
'''
#contoh 
#Digunakan selfuntuk mengakses properti kelas:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()

'''
Mengapa menggunakan diri sendiri?
Tanpa itu self, Python tidak akan tahu properti objek mana yang ingin Anda akses:
'''
#Contoh
'''Parameter tersebut selfmenghubungkan metode dengan objek tertentu:
''' 

class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()

#Diri Sendiri Tidak Harus Disebut "diri sendiri"
'''
Tidak harus diberi nama self, Anda bisa menyebutnya apa pun yang Anda suka, tetapi harus menjadi parameter pertama dari metode apa pun di dalam kelas tersebut:
'''
#Contoh
#Gunakan kata-kata myobject dan abc sebagai pengganti self :

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()

'''
Mengakses Properti dengan diri sendiri
Anda dapat mengakses properti apa pun dari kelas tersebut menggunakan self:
''' 
#Contoh
#Akses beberapa properti menggunakan self:

class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

'''
Memanggil Metode dengan diri sendiri
Anda juga dapat memanggil metode lain di dalam kelas menggunakan self:
'''
#Contoh
#Panggil satu metode dari metode lain menggunakan self:

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()

