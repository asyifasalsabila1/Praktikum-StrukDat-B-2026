'''
 SOAL LIST
📌 Soal:

Buat program yang:

Menyimpan daftar nilai 5 siswa dalam sebuah list

Menampilkan:

Nilai tertinggi

Nilai terendah

Rata-rata nilai

Tambahkan 1 nilai baru ke dalam list

Tampilkan list setelah ditambah

Jawaban:
'''
# Membuat list nilai siswa
nilai_siswa = [78, 85, 90, 66, 88]

print("Daftar Nilai Awal:", nilai_siswa)

# Mencari nilai tertinggi dan terendah
nilai_tertinggi = max(nilai_siswa)
nilai_terendah = min(nilai_siswa)

# Menghitung rata-rata
rata_rata = sum(nilai_siswa) / len(nilai_siswa)

print("Nilai Tertinggi:", nilai_tertinggi)
print("Nilai Terendah:", nilai_terendah)
print("Rata-rata Nilai:", rata_rata)

# Menambahkan nilai baru
nilai_baru = 92
nilai_siswa.append(nilai_baru)

print("Daftar Nilai Setelah Ditambah:", nilai_siswa)

'''
2. SOAL TUPLE
📌 Soal:

Simpan data koordinat suatu titik dalam bentuk tuple.
Tampilkan:

Nilai X

Nilai Y

Hitung jarak titik dari (0,0)

Jawaban:
'''
import math

# Tuple koordinat
titik = (6, 8)

print("Koordinat Titik:", titik)

x = titik[0]
y = titik[1]

print("Nilai X:", x)
print("Nilai Y:", y)

# Menghitung jarak dari titik (0,0)
jarak = math.sqrt(x**2 + y**2)

print("Jarak dari (0,0):", jarak)

'''
3️. SOAL SET
📌 Soal:

Buat program untuk:

Menyimpan daftar nama peserta lomba

Tambahkan beberapa nama yang sama

Tampilkan hasil akhirnya

Tampilkan jumlah peserta unik

Jawaban:
'''
# Membuat set peserta
peserta = {"Andi", "Budi", "Citra"}

# Menambahkan nama (termasuk duplikat)
peserta.add("Dewi")
peserta.add("Andi")  # Duplikat
peserta.add("Budi")  # Duplikat

print("Daftar Peserta Unik:")
for nama in peserta:
    print("-", nama)

print("Jumlah Peserta Unik:", len(peserta))

'''
4. SOAL DICTIONARY
📌 Soal:

Buat program yang:

Menyimpan data siswa (nama, umur, jurusan)

Ubah jurusan siswa

Tambahkan data alamat

Tampilkan seluruh data

Jawaban:
'''
# Membuat dictionary data siswa
siswa = {
    "nama": "Andi",
    "umur": 20,
    "jurusan": "Teknik Informatika"
}

print("Data Awal:", siswa)

# Mengubah jurusan
siswa["jurusan"] = "Sistem Informasi"

# Menambahkan alamat
siswa["alamat"] = "Jakarta"

print("\nData Setelah Diubah:")
for key, value in siswa.items():
    print(key, ":", value)

'''
5️.SOAL ARRAY
📌 Soal:

Buat program menggunakan module array untuk:

Menyimpan 5 angka

Menampilkan isi array

Menghitung total dan rata-rata

Jawaban:
'''
import array

# Membuat array tipe integer
angka = array.array('i', [10, 20, 30, 40, 50])

print("Isi Array:")
for a in angka:
    print(a)

# Menghitung total
total = sum(angka)

# Menghitung rata-rata
rata_rata = total / len(angka)

print("Total:", total)
print("Rata-rata:", rata_rata)