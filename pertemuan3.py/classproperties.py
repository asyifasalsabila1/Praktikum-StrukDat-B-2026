'''
Properti Kelas
Properti adalah variabel yang dimiliki oleh suatu kelas. Variabel ini menyimpan data untuk setiap objek yang dibuat dari kelas tersebut.

ContohDapatkan server Python Anda sendiri
Buat kelas dengan properti:
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

'''
Akses Properti
Anda dapat mengakses properti objek menggunakan notasi titik:

Contoh
Mengakses properti suatu objek:
'''
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

'''
Ubah Properti
Anda dapat memodifikasi nilai properti pada objek:

Contoh
Ubah properti usia:
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)

'''
Hapus Properti
Anda dapat menghapus properti dari objek menggunakan delkata kunci:

Contoh
Hapus properti usia:
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # This works
# print(p1.age) # This would cause an error

'''
Properti Kelas vs Properti Objek
Properti yang didefinisikan di dalamnya __init__()merupakan milik setiap objek (properti instans).

Properti yang didefinisikan di luar metode merupakan milik kelas itu sendiri (properti kelas) dan dimiliki bersama oleh semua objek:

Contoh
Properti kelas vs properti instance:
'''
class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

'''
Memodifikasi Properti Kelas
Saat Anda memodifikasi properti kelas, hal itu memengaruhi semua objek:

Contoh
Mengubah properti kelas:
'''
class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)

'''
Tambahkan Properti Baru
Anda dapat menambahkan properti baru ke objek yang sudah ada:

Contoh
Tambahkan properti baru ke sebuah objek:
'''
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)
