# Data awal
transaksi = [
    {"produk": "Buku", "harga": 10000, "jumlah": 3},
    {"produk": "Pena", "harga": 5000, "jumlah": 10},
    {"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]

# a. Ubah jumlah buku menjadi 8
for item in transaksi:
    if item["produk"] == "Buku":
        item["jumlah"] = 8
        print(transaksi)

# b. Tambahkan 2 produk baru
transaksi.append({"produk": "Pensil", "harga": 3000, "jumlah": 5})
transaksi.append({"produk": "Penggaris", "harga": 4000, "jumlah": 4})
print(transaksi)

# c. Hitung total pendapatan setiap transaksi
for item in transaksi:
    total = item["harga"] * item["jumlah"]
    print(f"Produk: {item['produk']} | Total: {total}")