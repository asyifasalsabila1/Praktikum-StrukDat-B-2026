class Motor:   # Membuat class bernama Motor
    def __init__(self, merek, warna, tahun):   # Constructor
        self.merek = merek
        self.warna = warna
        self.tahun = tahun

    def lampusen(self):   # Method untuk menyalakan lampu sein
        print("Lampu sein menyala warna kuning")

    def bunyi(self):   # Method untuk mengeluarkan suara motor
        print("Brumm brumm")

    def ubah_merek(self, merek_baru):   # Method untuk mengubah merek
        self.merek = merek_baru

# Membuat 3 object
kendaraan1 = Motor("Supra", "Biru", 2015)
kendaraan2 = Motor("King", "Hitam", 2013)
kendaraan3 = Motor("Beat", "Hijau", 2012)

# Menampilkan data awal
print(kendaraan1.merek, kendaraan1.warna, kendaraan1.tahun)
print(kendaraan2.merek, kendaraan2.warna, kendaraan2.tahun)
print(kendaraan3.merek, kendaraan3.warna, kendaraan3.tahun)

# Memanggil method
kendaraan1.lampusen()
kendaraan2.bunyi()

# Mengubah salah satu atribut
print("Sebelum diubah:", kendaraan1.merek)
kendaraan1.ubah_merek("Vario")
print("Sesudah diubah:", kendaraan1.merek)
