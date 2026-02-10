'''
4. Sebuah data mahasiswa disimpan dalam bentuk dictionary:
mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika",
"ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "Sistem
Informasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika",
"ipk": 3.75}
}
1. Tampilkan nama mahasiswa yang memiliki IPK di atas 3.5.
2. Hitung rata-rata IPK seluruh mahasiswa.
3. Tambahkan satu data mahasiswa baru ke dalam dictionary tersebut.
'''
mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "SistemInformasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika",
"ipk": 3.75}
} #membuat dictionary dengan key nim dan valuenya berupa nama, prodi, dan IPK

#1. tampilkan nama mahasiswa yang di ipk 3.5
for x in mahasiswa: #unutk setiap x di dict mahasiswa
    if (mahasiswa[x]["ipk"]) > 3.5: #jika IPK > 3.5
        print(mahasiswa[x]["nama"]) #menampilkan nama yang memiliki IPK >3.5
#2. menghitung rata
jumlah = 0 #untuk menyimpan total IPK
hitung = 0 #untuk menyimpan jumlah mahasiswa
for x in mahasiswa : #untuk setiap x pada dict mahasiswa
    jumlah = jumlah + (mahasiswa[x]["ipk"]) #perulangan untuk menjumlahkan IPK
    hitung = hitung + 1 #menambahkan IPK ke variabel jumlah
    rata = jumlah / hitung #menghitung rata - rata
print (rata) #menampilkan rata arat
#3. menambahkan satu data
mahasiswa ["A004"] = {"nama": "asyifa", "prodi": "Informatika", "ipk": 4.00} 
print(mahasiswa) #menampilkan seluruh dict