nilai_tugas = [70, 85, 90, 65, 80]
index_nilai = nilai_tugas.index(65)

nilai_tugas[3] = 75
print(nilai_tugas)

nilai_tugas = [70, 85, 90, 65, 80]
nilai_tugas.append(95)
nilai_tugas.sort(reverse=True)
print(nilai_tugas)

nilai_tugas = [70, 85, 90, 65, 80]
total = sum(nilai_tugas)
print(total)



if 100 in nilai_tugas:
    print("Ada nilai sempurna")
else:
    print("Tidak ada")




