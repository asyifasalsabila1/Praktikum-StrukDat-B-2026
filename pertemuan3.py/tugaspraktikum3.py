class Motor:
    def __init__(self,merek,warna,tahun):
        self.merek=merek
        self.warna=warna
        self.tahun=tahun

    def lampusen (self):
        print("kuning")

    def bunyi (self):
        print("brumm brumm")

    def ubahmerek(self,merekbaru):
        self.merek=merekbaru

kendaraan1=Motor("supra","biru","2015")
kendaraan2=Motor("king", "hitam", "2013") 
kendarran3=Motor("beat" ,"hijau" ,"2012")

kendaraan1.lampusen()
kendaraan1 = "supra"
print(f"sebelum di ubah : {kendaraan1}")





 