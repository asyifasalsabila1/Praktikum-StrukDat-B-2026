'''
argumen - parameter 
Buat fungsi sapa(nama) yang:

Menerima 1 parameter

Menampilkan pesan sambutan

Dipanggil dengan 3 argumen berbeda

 Jawaban:
'''
def sapa(nama):
    print("===================================")
    print("Halo,", nama + "!")
    print("Selamat datang di sistem kami.")
    print("Semoga harimu menyenangkan.")
    print("===================================")
    print()

# Pemanggilan fungsi dengan argumen berbeda
sapa("Andi")
sapa("Budi")
sapa("Citra")

'''
SOAL 2 — Jumlah Argumen Harus Sesuai
Soal:

Buat fungsi hitung_luas_persegi_panjang(panjang, lebar)
Fungsi harus mengembalikan luas.
 Jawaban:

'''
def hitung_luas_persegi_panjang(panjang, lebar):
    print("Menghitung luas persegi panjang...")
    luas = panjang * lebar
    print("Panjang:", panjang)
    print("Lebar:", lebar)
    print("Luas:", luas)
    return luas

# Pemanggilan benar
hasil = hitung_luas_persegi_panjang(10, 5)
print("Hasil return:", hasil)
print()

# Pemanggilan salah (akan error)
# hitung_luas_persegi_panjang(10)

'''
 SOAL 3 — Default Parameter
Soal:
Buat fungsi hitung_gaji(nama, gaji_pokok=3000000)

Jawaban:

'''
def hitung_gaji(nama, gaji_pokok=3000000):
    print("===================================")
    print("Nama Karyawan:", nama)
    print("Gaji Pokok:", gaji_pokok)
    print("Total Gaji yang diterima:", gaji_pokok)
    print("===================================")
    print()
    return gaji_pokok

# Dengan gaji sendiri
hitung_gaji("Andi", 5000000)

# Tanpa gaji (pakai default)
hitung_gaji("Budi")
'''
SOAL 4 — Keyword Argument
Soal:

Buat fungsi data_siswa(nama, umur, jurusan)
Panggil dengan positional dan keyword.

Jawaban:
'''
def data_siswa(nama, umur, jurusan):
    print("===== DATA SISWA =====")
    print("Nama:", nama)
    print("Umur:", umur)
    print("Jurusan:", jurusan)
    print("======================")
    print()

# Positional argument
data_siswa("Andi", 20, "Informatika")

# Keyword argument (urutan bebas)
data_siswa(jurusan="Sistem Informasi", nama="Budi", umur=22)
'''
 SOAL 5 — Positional-Only Argument (/)
Soal:

Buat fungsi login dengan positional-only.

 Jawaban:
'''
def login(username, password, /):
    print("Memproses login...")
    print("Username:", username)
    print("Password:", password)
    print("Login berhasil!")
    print()

# Benar
login("admin", "12345")

# Salah (akan error)
# login(username="admin", password="12345")
'''
 SOAL 6 — Keyword-Only Argument (*)
Soal:

Buat fungsi transfer uang yang hanya menerima keyword argument.

 Jawaban:
'''
def transfer_uang(*, pengirim, penerima, jumlah):
    print("===== TRANSFER UANG =====")
    print("Dari:", pengirim)
    print("Ke:", penerima)
    print("Jumlah:", jumlah)
    print("Transfer berhasil!")
    print()

# Benar
transfer_uang(pengirim="Andi", penerima="Budi", jumlah=100000)

# Salah (akan error)
# transfer_uang("Andi", "Budi", 100000)
'''
 SOAL 7 — Gabungan Semua Konsep
Soal:

Buat fungsi:

def transaksi(kode_transaksi, /, nama_barang, jumlah=1, *, diskon):
 Jawaban:
'''
def transaksi(kode_transaksi, /, nama_barang, jumlah=1, *, diskon):
    print("===== DETAIL TRANSAKSI =====")
    print("Kode Transaksi:", kode_transaksi)
    print("Nama Barang:", nama_barang)
    print("Jumlah:", jumlah)

    harga_satuan = 50000
    total = harga_satuan * jumlah
    potongan = total * (diskon / 100)
    total_bayar = total - potongan

    print("Harga Satuan:", harga_satuan)
    print("Total Sebelum Diskon:", total)
    print("Diskon:", diskon, "%")
    print("Total Setelah Diskon:", total_bayar)
    print("============================")
    print()

    return total_bayar


# Pemanggilan benar
hasil_transaksi = transaksi("TRX001", "Laptop", 2, diskon=10)
print("Total yang harus dibayar:", hasil_transaksi)