kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]

nama = "Budi"
nilai = 70

for nama, nilai in kumpulan_nilai: 
 if nilai >= 75:
    print(f"Selamat {nama}, Anda Lulus!")
else:
    print(f"Maaf {nama}, Anda harus remidi.")