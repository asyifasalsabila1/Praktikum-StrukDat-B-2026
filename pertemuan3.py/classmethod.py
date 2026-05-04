'''
Metode Kelas
Metode adalah fungsi yang dimiliki oleh suatu kelas. Metode mendefinisikan perilaku objek yang dibuat dari kelas tersebut.

ContohDapatkan server Python Anda sendiri
Buat sebuah metode dalam sebuah kelas:
'''
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()

'''
Metode dengan Parameter
Metode dapat menerima parameter seperti halnya fungsi biasa:

Contoh
Buat metode dengan parameter:
'''
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

'''
Metode Mengakses Properti
Metode dapat mengakses dan memodifikasi properti objek menggunakan self:

Contoh
Metode yang mengakses properti objek:
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())

'''
Metode untuk Memodifikasi Sifat-Sifat
Metode dapat memodifikasi properti suatu objek:

Contoh
Metode yang mengubah nilai properti:
'''
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

'''
Metode __str__()
Metode ini __str__()adalah metode khusus yang mengontrol apa yang dikembalikan saat objek dicetak:

Contoh
Tanpa __str__()metode tersebut:
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1)
#Contoh
#Dengan __str__()metode:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)

'''
Berbagai Metode
Suatu kelas dapat memiliki beberapa metode yang bekerja bersama-sama:

Contoh
Buat beberapa metode dalam sebuah kelas:
'''
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

'''
Metode Penghapusan
Anda dapat menghapus metode dari sebuah kelas menggunakan delkata kunci:

Contoh
Menghapus sebuah metode dari sebuah kelas:

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")

del Person.greet

p1.greet() # This will cause an error
Latih
'''