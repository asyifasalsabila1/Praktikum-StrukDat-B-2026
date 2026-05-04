sesi_pagi = {"Andi", "Budi", "Cici"}
sesi_siang = {"Budi", "Deni", "Eka"}

# a. Mahasiswa yang hadir di kedua sesi
hadir_keduanya = sesi_pagi & sesi_siang

# b & c. Daftar unik mahasiswa (gabungan kedua sesi)
sesi_hari_ini = sesi_pagi | sesi_siang

print("Hadir pagi DAN siang:", hadir_keduanya)
print("Daftar mahasiswa unik hari ini:", sesi_hari_ini)
print("Total mahasiswa unik:", len(sesi_hari_ini))