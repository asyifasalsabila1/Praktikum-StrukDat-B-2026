'''
DICTIONARY (INPUT DATA)
📌 Soal:

Buat program untuk input data mahasiswa (nama + 3 nilai) ke dalam dictionary.


data = {}

jumlah = int(input("Jumlah mahasiswa: "))

for i in range(jumlah):
    nama = input("Nama: ")
    n1 = int(input("Nilai 1: "))
    n2 = int(input("Nilai 2: "))
    n3 = int(input("Nilai 3: "))
    data[nama] = (n1, n2, n3)

print(data)
 
#Jumlah mahasiswa: 1
Nama: Andi
Nilai 1: 80
Nilai 2: 90
Nilai 3: 85

{'Andi': (80, 90, 85)}

🔹 2. HITUNG RATA-RATA
📌 Soal:

Hitung rata-rata dari tuple nilai.


nilai = (80, 90, 85)

total = 0
for x in nilai:
    total += x

rata = total / len(nilai)

print("Rata-rata:", rata)


 
Rata-rata: 85.0


🔹 3. IF (GRADE)
📌 Soal:

Tentukan grade dari nilai rata-rata.


rata = 85

if rata >= 85:
    grade = "A"
elif rata >= 70:
    grade = "B"
else:
    grade = "C"

print("Grade:", grade)

Grade: A


🔹 4. SELECTION SORT
Soal:

Urutkan data berikut (descending):

[("Andi", 85), ("Budi", 75)]

data = [("Andi", 85), ("Budi", 75)]

n = len(data)

for i in range(n):
    max_idx = i
    for j in range(i+1, n):
        if data[j][1] > data[max_idx][1]:
            max_idx = j

    data[i], data[max_idx] = data[max_idx], data[i]

print(data)


[('Andi', 85), ('Budi', 75)]

🔹 5. RANKING
 Soal:

Tampilkan ranking dari data yang sudah diurutkan.


data = [("Andi", 85), ("Budi", 75)]

for i, item in enumerate(data):
    print(f"{i+1}. {item[0]} - {item[1]}")



1. Andi - 85
2. Budi - 75


 6. MATRIX (BONUS)
 Soal:

Hitung total matriks berikut:

[
    [1, 2],
    [3, 4]
]


mat = [
    [1, 2],
    [3, 4]
]

total = 0

for row in mat:
    for val in row:
        total += val

print("Total:", total)


Total: 10
KESIMPULAN (POLA JELAS BANGET)

'''