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