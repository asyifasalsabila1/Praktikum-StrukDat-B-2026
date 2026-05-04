'''
Pewarisan Python
Pewarisan memungkinkan kita untuk mendefinisikan sebuah kelas yang mewarisi semua metode dan properti dari kelas lain.

Kelas induk adalah kelas yang diwarisi, juga disebut kelas dasar.

Kelas anak adalah kelas yang mewarisi dari kelas lain, juga disebut kelas turunan.

Buat Kelas Induk
Kelas apa pun dapat menjadi kelas induk, jadi sintaksnya sama seperti membuat kelas lainnya:

ContohDapatkan server Python Anda sendiri
Buat kelas bernama Person, dengan properti firstnamedan , serta sebuah metode:lastnameprintname
'''
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

'''
Buat Kelas Turunan
Untuk membuat kelas yang mewarisi fungsionalitas dari kelas lain, kirimkan kelas induk sebagai parameter saat membuat kelas turunan:

Contoh
Buat kelas bernama Student, yang akan mewarisi properti dan metode dari Personkelas:
'''
class Student(Person):
  pass

#Sekarang kelas Student memiliki properti dan metode yang sama dengan kelas Person.

#Contoh
#Gunakan Studentkelas tersebut untuk membuat objek, lalu jalankan printnamemetodenya:

x = Student("Mike", "Olsen")
x.printname()

'''
Tambahkan fungsi __init__()
Sejauh ini kita telah membuat kelas turunan yang mewarisi properti dan metode dari kelas induknya.

Kami ingin menambahkan __init__()fungsi tersebut ke kelas turunan (bukan ke passkata kunci).
Contoh
Tambahkan __init__()fungsi ke dalam Studentkelas:
'''
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
    '''
    Untuk mempertahankan pewarisan fungsi induk __init__() , tambahkan panggilan ke fungsi induk __init__():

Contoh
'''
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

'''
Gunakan fungsi super()
Python juga memiliki super()fungsi yang akan membuat kelas turunan mewarisi semua metode dan properti dari kelas induknya:

Contoh
'''
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

    #Tambahkan Properti
#Contoh
#Tambahkan properti bernama graduationyearke Studentkelas:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

    #Pada contoh di bawah ini, tahun 2019harus berupa variabel, dan diteruskan ke Studentkelas saat membuat objek siswa. Untuk melakukannya, tambahkan parameter lain dalam __init__()fungsi tersebut:

#Contoh
#Tambahkan yearparameter, dan berikan tahun yang benar saat membuat objek:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

#Tambahkan Metode
#Contoh
#Tambahkan metode bernama welcomeke dalam Studentkelas:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)