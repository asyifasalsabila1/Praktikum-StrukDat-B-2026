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


