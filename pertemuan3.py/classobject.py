'''
Kelas/Objek Python 
Python adalah bahasa pemrograman berorientasi objek.Hampir semua hal di Python adalah objek, dengan properti dan metodenya masing-masing.
Sebuah Class itu seperti konstruktor objek, atau "cetak biru" untuk membuat objek.
'''

#Buat Kelas
'''
Untuk membuat kelas, gunakan kata kunci class:

ContohDapatkan server Python Anda sendiri
Buat kelas bernama MyClass, dengan properti bernama x:
'''
class MyClass:
  x = 5

'''
Buat Objek
Sekarang kita dapat menggunakan kelas bernama MyClass untuk membuat objek:

Contoh
Buat objek bernama p1, dan cetak nilai x:
'''
p1 = MyClass()
print(p1.x)

'''
Hapus Objek
Anda dapat menghapus objek dengan menggunakan delkata kunci:

Contoh
Hapus objek p1:
'''
del p1

'''
Beberapa Objek
Anda dapat membuat beberapa objek dari kelas yang sama:

Contoh
Buat tiga objek dari kelas MyClass:
'''
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)