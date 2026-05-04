#class object seperti 
#clas  fruit  object ny apple,banana ,mango
#clas car object ny volvo,audi,toyota

#apa itu pascal case 
#camel case  penamaan variabel  menggunakan (-)
#class ada init method




class init:
  class Car:
    def __init__(self, merek, warna, tahun):
        self.merek = merek
        self.warna = warna
        self.tahun = tahun

p1 = car("Toyota","merah",2025)
p2 = car("lambo", "kuning", "2026") 
p3 = car("inova" ,"hijau" ,"2019")

def klakson (self):
 print("tit tiiiit")

def intro(self):
 print(f"merk: ")
print(p1)

#
class MyClass:
  x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#init method  
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# objek pertama
p1 = Person("Emil", 36)
print(p1.name)
print(p1.age)  #output =emil 36

#class Person:  pass
p2 = Person("Tobias", 25)
print(p2.name)
print(p2.age)

print(p1.name)
print(p1.age)  #output tobies 25

#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)


p1 = Person("Emil", 25)
p1.greet()    #hello my name is emil 

#
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)  #output emil 36

#Mengakses properti suatu objek:

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

#Buat metode dengan parameter:

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

#Metode yang mengubah nilai properti:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

#Tanpa __str__()metode tersebut:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1)


#Buat beberapa metode dalam sebuah kelas:

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()