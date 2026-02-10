'''
3. Diberikan dua set mata kuliah pilihan:
kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}
1. Tentukan mata kuliah yang diambil oleh kedua kelas.
2. Tentukan mata kuliah yang hanya diambil kelas A.
3. Tentukan seluruh mata kuliah unik yang diambil oleh kelas A dan B.
'''

#membuat set mata kuliah yang diambil oleh kelas A
kelas_A = {"Struktur Data", "Basis Data", "AI","Pemrograman Web"} 


#membuat set mata kuliah yang diambil oleh kelas B
kelas_B = {"Struktur Data", "Machine Learning", "AI","Cloud Computing"}

#mata kuliah yang diambil oleh kedua kelas
matakuliahyangsama = kelas_A.intersection(kelas_B) #akan memunculkan mata kuliah yang sama diambil oleh kedua kelas
print(matakuliahyangsama) #menampilkan hasil ke layar

#mata kuliah yang hanya diambil oleh kelas a
print("Mata kuliah yang diambil oleh kelas A", kelas_A) #menampilkan mata kuliah yang hanya diambil oleh kelas A

#seluruh mata kuliah unik yang diambil oleh kelas A dan B
matakuliah =kelas_A.union(kelas_B) #menggabungkan mata kuliah yang diambil
print("seluruh mata kuliah yang diambil oleh kedua kelas",matakuliah) #menampilkan mata kuliah yang diambil kedua kelas
