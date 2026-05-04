'''
Semua kelas memiliki metode bawaan yang disebut __init__(), yang selalu dieksekusi ketika kelas tersebut diinisialisasi.
Metode ini __init__()digunakan untuk menetapkan nilai pada properti objek, atau untuk melakukan operasi yang diperlukan saat objek sedang dibuat.
'''
#Buat kelas bernama Person, gunakan __init__()metode tersebut untuk menetapkan nilai untuk nama dan usia:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)   # output Emil 36

'''
Mengapa Menggunakan __init__()?
Tanpa __init__()metode tersebut, Anda perlu mengatur properti secara manual untuk setiap objek:
'''
#Contoh
#Buat kelas tanpa __init__():

class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

'''
Penggunaan ini __init__()mempermudah pembuatan objek dengan nilai awal:

Contoh
Dengan __init__(), Anda dapat mengatur nilai awal saat membuat objek:
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)


'''
Nilai Default di __init__()
Anda juga dapat mengatur nilai default untuk parameter dalam __init__()metode tersebut:

Contoh
Tetapkan nilai default untuk parameter usia:
'''
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

'''
Beberapa Parameter
Metode ini __init__()dapat memiliki parameter sebanyak yang Anda butuhkan:

Contoh
Buat kelas Person dengan beberapa parameter:
'''
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
