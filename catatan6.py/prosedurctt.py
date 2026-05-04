
'''
rosedur garis()

Mencetak garis pembatas sepanjang 40 karakter =

2. Prosedur input_data()

Meminta input:

Nama siswa

Nilai UTS

Nilai UAS

Menampilkan kembali data yang sudah diinput

(Tidak boleh return, langsung tampilkan)

3️⃣ Prosedur hitung_rata_rata(nilai1, nilai2)

Menghitung rata-rata

Menampilkan hasil rata-rata

Tidak boleh menggunakan return

4️⃣ Prosedur tentukan_kelulusan(rata_rata)

Jika rata-rata ≥ 75 → LULUS

Jika < 75 → TIDAK LULUS

Tampilkan hasilnya

📌 Program Utama:

Panggil semua prosedur di atas

Gunakan urutan yang benar

✅ JAWABAN LENGKAP
'''

# =========================================
# PROSEDUR 1 - Garis Pembatas
# =========================================
def garis():
    print("=" * 40)


# =========================================
# PROSEDUR 2 - Input Data
# =========================================
def input_data():
    garis()
    print("INPUT DATA SISWA")
    garis()

    nama = input("Masukkan nama siswa: ")
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    garis()
    print("DATA YANG DIINPUT")
    print("Nama :", nama)
    print("Nilai UTS :", uts)
    print("Nilai UAS :", uas)
    garis()

    # Panggil prosedur lain langsung
    hitung_rata_rata(uts, uas)


# =========================================
# PROSEDUR 3 - Hitung Rata-rata
# =========================================
def hitung_rata_rata(nilai1, nilai2):
    rata = (nilai1 + nilai2) / 2

    print("Rata-rata Nilai :", rata)

    # Lanjut cek kelulusan
    tentukan_kelulusan(rata)


# =========================================
# PROSEDUR 4 - Tentukan Kelulusan
# =========================================
def tentukan_kelulusan(rata_rata):
    if rata_rata >= 75:
        print("Status : LULUS")
    else:
        print("Status : TIDAK LULUS")

    garis()


# =========================================
# PROGRAM UTAMA
# =========================================
input_data()



✅ soal1.py
# soal1.py

def tambah_buku(nama, harga, stok):
    if harga <= 0:
        print("Error: Harga harus lebih besar dari 0.")
        return None
    if stok < 0:
        print("Error: Stok tidak boleh negatif.")
        return None
    
    return {
        "nama": nama,
        "harga": harga,
        "stok": stok
    }


# Program Utama
daftar_buku = []

for i in range(3):
    print(f"\nInput Buku ke-{i+1}")
    nama = input("Nama Buku: ")
    try:
        harga = float(input("Harga Buku: "))
        stok = int(input("Stok Buku: "))
    except ValueError:
        print("Input harga/stok tidak valid!")
        continue

    buku = tambah_buku(nama, harga, stok)
    if buku is not None:
        daftar_buku.append(buku)

print("\n=== Daftar Buku Berhasil Ditambahkan ===")
for buku in daftar_buku:
    print(buku)
✅ soal2.py
# soal2.py

katalog = [
    {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
    {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]

def cari_buku(katalog, keyword):
    hasil = []
    keyword = keyword.lower()

    for buku in katalog:
        if keyword in buku['nama'].lower():
            hasil.append(buku)

    if not hasil:
        print("Buku tidak ditemukan.")
    
    return hasil


# Program Utama
keyword = input("Masukkan keyword pencarian: ")
hasil_pencarian = cari_buku(katalog, keyword)

if hasil_pencarian:
    print("\n=== Hasil Pencarian ===")
    for buku in hasil_pencarian:
        print(f"Nama : {buku['nama']}")
        print(f"Harga: Rp {buku['harga']}")
        print(f"Stok : {buku['stok']}")
        print("-" * 30)
✅ soal3.py
# soal3.py

katalog = [
    {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
    {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]

riwayat_transaksi = set()

def proses_transaksi(katalog, nama_buku, jumlah_beli):
    for buku in katalog:
        if buku['nama'].lower() == nama_buku.lower():
            if buku['stok'] >= jumlah_beli:
                total = buku['harga'] * jumlah_beli
                buku['stok'] -= jumlah_beli
                print(f"Total harga: Rp {total}")
                riwayat_transaksi.add(buku['nama'])
            else:
                print("Stok tidak mencukupi.")
            return
    print("Buku tidak ditemukan.")


# Program Utama (3 transaksi)
for i in range(3):
    print(f"\nTransaksi ke-{i+1}")
    nama = input("Nama Buku: ")
    jumlah = int(input("Jumlah beli: "))
    proses_transaksi(katalog, nama, jumlah)

print("\n=== Riwayat Transaksi ===")
for nama in riwayat_transaksi:
    print(nama)
✅ soal4.py
# soal4.py

level_diskon = (
    (500000, 15),
    (300000, 10),
    (100000, 5),
    (0, 0),
)

def hitung_diskon(total_belanja, level_diskon, index=0):
    if index >= len(level_diskon):
        return (0, 0, total_belanja)

    def hitung_diskon(total_belanja, level_diskon, index=0):
    if index >= len(level_diskon):
        return (0, 0, total_belanja)

# Program Utama
nama = input("Nama Pelanggan: ")
total_belanja = float(input("Total Belanja: "))

persen, nominal, total_bayar = hitung_diskon(total_belanja, level_diskon)

print("\n=== Rincian Diskon ===")
print(f"Total Belanja : Rp {total_belanja}")

if total_belanja < 100000:
    print("Tidak ada diskon")
else:
    print(f"Diskon        : {persen}%")
    print(f"Nominal Diskon: Rp {nominal}")

print(f"Total Bayar   : Rp {total_bayar}")
✅ soal5.py (Integrasi Lengkap)
# soal5.py

katalog = []
log_transaksi = []
riwayat_transaksi = set()

level_diskon = (
    (500000, 15),
    (300000, 10),
    (100000, 5),
    (0, 0),
)

def tambah_buku(nama, harga, stok):
    if harga <= 0:
        print("Error: Harga harus lebih besar dari 0.")
        return None
    if stok < 0:
        print("Error: Stok tidak boleh negatif.")
        return None
    
    return {"nama": nama, "harga": harga, "stok": stok}


def proses_transaksi(katalog, nama_buku, jumlah_beli):
    for buku in katalog:
        if buku['nama'].lower() == nama_buku.lower():
            if buku['stok'] >= jumlah_beli:
                total = buku['harga'] * jumlah_beli
                buku['stok'] -= jumlah_beli
                riwayat_transaksi.add(buku['nama'])
                log_transaksi.append((buku['nama'], jumlah_beli, total))
                print(f"Total harga: Rp {total}")
            else:
                print("Stok tidak mencukupi.")
            return
    print("Buku tidak ditemukan.")


def hitung_diskon(total_belanja, level_diskon, index=0):
    if index >= len(level_diskon):
        return (0, 0, total_belanja)

    batas, persen = level_diskon[index]

    if total_belanja >= batas:
        nominal_diskon = total_belanja * persen / 100
        total_bayar = total_belanja - nominal_diskon
        return (persen, nominal_diskon, total_bayar)
    else:
        return hitung_diskon(total_belanja, level_diskon, index + 1)


while True:
    print("\n=== PyBook Store ===")
    print("1. Tambah Buku")
    print("2. Tampilkan Semua Buku")
    print("3. Beli Buku")
    print("4. Laporan Penjualan")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Nama Buku: ")
        harga = float(input("Harga: "))
        stok = int(input("Stok: "))
        buku = tambah_buku(nama, harga, stok)
        if buku:
            katalog.append(buku)

    elif pilihan == "2":
        print("\n=== Daftar Buku ===")
        print(f"{'Nama':20} {'Harga':10} {'Stok':5}")
        for buku in katalog:
            print(f"{buku['nama']:20} {buku['harga']:10} {buku['stok']:5}")

    elif pilihan == "3":
        nama = input("Nama Buku: ")
        jumlah = int(input("Jumlah beli: "))
        proses_transaksi(katalog, nama, jumlah)

    elif pilihan == "4":
        print("\n=== Laporan Penjualan ===")
        total_pemasukan = sum(t[2] for t in log_transaksi)
        print(f"Total Pemasukan: Rp {total_pemasukan}")

        frekuensi = {}
        for nama, jumlah, total in log_transaksi:
            frekuensi[nama] = frekuensi.get(nama, 0) + jumlah

        if frekuensi:
            buku_terlaris = max(frekuensi, key=frekuensi.get)
            print(f"Buku Terlaris: {buku_terlaris}")
        else:
            print("Belum ada transaksi.")

    elif pilihan == "5":
        print("Terima kasih telah menggunakan PyBook Store!")
        break

    else:
        print("Pilihan tidak