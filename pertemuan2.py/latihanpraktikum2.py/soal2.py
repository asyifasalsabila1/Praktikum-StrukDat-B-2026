"""
2. Diberikan sebuah tuple data mahasiswa:
mahasiswa = ("A001", "Budi", "Informatika")
1. Tampilkan nama mahasiswa dari tuple tersebut.
2. Tampilkan seluruh isi tuple menggunakan perulangan for.
3. Jelaskan satu alasan mengapa tuple tidak bisa diubah.
"""
#tampilkan nama mahasiswa
mahasiswa = ("A001", "Budi", "Informatika") #tuple bernama mahasiswa yang berisi nama, nim, dan prodi
print(mahasiswa[1]) #menampilkan index ke-1 pada tuple

#menggunakan perulangan for
for x in mahasiswa: #untuk setiap x pada tuple mahasiswa
    print (x) #menampilkan satu per satu elemen

"""
tuple tidak bisa diubah karena yang bisa diubah itu adalah list
"""
   