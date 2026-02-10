"""
1. Diberikan sebuah list angka:
angka = [10, 20, 30, 40, 50]
1. Tambahkan angka 60 ke dalam list.
2. Hapus angka 20 dari list.
3. Tampilkan angka tertinggi dan terendah
4. Hitung rata-rata angka setelah perubahan data
5. Tampilkan seluruh isi list setelah perubahan.
"""
#1. tambahkan angka 60
angka = [10, 20, 30, 40, 50]  #membuat list bernama angka yang diisi dengan beberapa bilangan

angka.append(60) #menggunakan perintah angka.append(60), untuk menambahkan nilai 60 ke bangian akhir dari list

print(angka) #menampilkan output dengan perintah print(angka)

#2. menghapus angka 20
angka.remove(20) #menggunakan perintah angka.remove(20) untuk menghapus nilai 20 dari dalam list

angka.sort(reverse=True) #menggunakan perintah angka.sort(reverse=True) untuk mengurutkan elemen list secara menurun


#menampilkan angka tertinggi dan terendah
tertinggi = max(angka) #menyimpan angka tertinggi dari list angka
terendah = min(angka) #menyimpan angka terendah dari list angka

print(tertinggi) #menampilkan angka tertinggi
print(terendah) #menampilkan angka terendah

print(angka)
#3. menghitung rata rata
total = 0 #untuk menyimpan jumlah seluruh angka.
jumlah = 0 #untuk menyimpan banyaknya elemen dalam list

#melakukan perulangan for untuk menjumlahkan angka
for x in angka :  #untuk setiap x pada angka
    total += x #menjumlahkan setiap elemen
    jumlah += 1 #menghitung jumlah elemen
    rata = total / jumlah #operasi untuk menghitung rata - rata
print("rata rata nya adalah ", rata) #menampilkan rata - rata ke layar