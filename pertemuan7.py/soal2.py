# 2. Case: Sistem Antrean Pasien (Emergency Room)
# Skenario: Di sebuah rumah sakit, pasien datang dengan tingkat urgensi yang berbeda. Secara
# default, pasien baru akan mengantre di belakang. Namun, jika ada pasien "Darurat", mereka harus
# disisipkan di posisi tertentu (misalnya posisi ke-2) agar segera ditangani setelah pasien pertama
# yang sedang diperiksa.
# Data Awal (Antrean saat ini): ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

# Tugas 1: Implementasi pada List Array
# Gunakan list bawaan Python antrean_array.
# 1. Buat list antrean_array dengan data awal di atas.
# 2. Buat fungsi sisipkan_pasien_darurat_array(nama_pasien, posisi):
# o Gunakan metode .insert(posisi - 1, nama_pasien).
# o Analisis: Apa yang terjadi pada pasien di belakangnya saat pasien baru masuk di
# tengah?
# 3. Cetak antrean akhir.

# Tugas 2: Implementasi pada Singly LinkedList
# Gunakan class Node dan AntreanLinkedList.
# 1. Implementasikan fungsi insert_at_position(head, nama_pasien, posisi) seperti kode yang
# kamu punya sebelumnya (menggunakan logika position - 2).
# 2. Tugas Tambahan: Tambahkan validasi sederhana. Jika posisi yang dimasukkan lebih besar
# dari jumlah pasien yang ada, maka pasien tersebut otomatis diletakkan di paling akhir (Append).

#TUGAS 1
antrean_array = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

def sisipkan_pasien_darurat_array(nama_pasien, posisi):
    antrean_array.insert(posisi-1, nama_pasien)
    return antrean_array

print(sisipkan_pasien_darurat_array("Pasien D (Kritis)", 1))



#TUGAS 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class HistoryLinkedList:
    def __init__(self):
        self.head = None

def traverseAndPrint(head):
    currentPosition = head
    while currentPosition:
        print(currentPosition.data, end=" -> ")
        currentPosition = currentPosition.next
    print("null")

#IMPLEMENTASI INSERT
def insert_at_position(head, nama_pasien, posisi):
    if posisi == 0:
        nodeBaru.next = head
        return nodeBaru

        currentPosition = head
    for _ in range(posisi-2):
        if currentPosition is None:
            break
        currentPosition = currentPosition.next

    nama_pasien.next = currentPosition.next
    currentPosition.next = nodeBaru
    return head

node1 = Node("Pasien A (Stabil)")
node2 = Node("Pasien B (Stabil)")
node3 = Node("Pasien C (Stabil)")

node1.next = node2
node2.next = node3

nodeBaru = Node("Pasien D (Kritis)")
node1 = insert_at_position(node1, nodeBaru, 0)

print(traverseAndPrint(node1))

#VALIDASI
def validasi(self, nama_pasien, posisi):
    if currentPosition is None and posisi > 1:
        currentPosition = self.head
        while currentPosition.next:
            currentPosition = currentPosition.next
        currentPosition.next = nodeBaru